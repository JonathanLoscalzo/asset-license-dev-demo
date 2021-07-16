from bson.objectid import ObjectId as BsonObjectId
from pydantic.main import BaseModel


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError("ObjectId required")
        return str(v)


class BaseMongoModel(BaseModel):
    _id: PydanticObjectId