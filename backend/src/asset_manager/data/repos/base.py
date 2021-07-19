from typing import Any, List, TypeVar, Generic
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument
from pymongo.database import Database
from asset_manager.data.exceptions import ItemNotFound

from asset_manager.data.schemas.base import BaseMongoModel

T = TypeVar("T", bound=BaseMongoModel)


class MongoRepository(Generic[T]):
    def __init__(self, db: Database, collection_name: str, generic_class: T):
        self.db = db
        self.collection_name = collection_name
        self.generic_class = generic_class

    def collection(self):
        return self.db.get_collection(self.collection_name)

    def get_all(self):
        return list(
            map(self.generic_class.parse_obj, self.collection().find({}))
        )

    def get(self, id: str) -> T:

        oid = ObjectId(id) if ObjectId.is_valid(id) else id
        item = self.collection().find_one({"$or": [{"id": id}, {"_id": oid}]})

        if item is None:
            raise ItemNotFound(id)

        return self.generic_class(**item)

    def get_by_filter(self, filter: dict) -> T:
        return self.collection().find_one(filter)

    def get_all_by_filter(self, filter: dict) -> List[T]:
        return list(map(self.generic_class.parse_obj, self.collection().find(filter)))

    def add(self, obj: T) -> Any:
        return self.collection().insert_one(obj.dict()).inserted_id

    def update(self, id, obj) -> Any:
        return self.find_and_update(id, {}, obj)

    def find_and_update(self, id, filter: dict, obj) -> Any:
        oid = ObjectId(id) if ObjectId.is_valid(id) else id
        res = self.collection().find_one_and_update(
            {"$or": [{"id": id}, {"_id": oid}], **filter},
            obj,
            return_document=ReturnDocument.AFTER,
        )

        return res

    def find_all_and_update(self, filter: dict, obj) -> Any:
        res = self.collection().update_many(
            {**filter},
            obj,
            upsert=True,
        )

        return res

    def remove(self, id) -> Any:
        raise NotImplementedError()
