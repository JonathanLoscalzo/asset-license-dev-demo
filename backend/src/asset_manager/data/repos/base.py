from typing import TypeVar, Generic
from pymongo.database import Database
from asset_manager.data.repos.exceptions import ItemNotFound

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

    def get(self, id: str):

        item = self.collection().find_one({"$or": [{"id": id}, {"_id": id}]})

        if item is None:
            raise ItemNotFound(id)

        return self.generic_class(
            **item
        )
