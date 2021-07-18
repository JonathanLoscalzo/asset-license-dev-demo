from typing import List, Union
from asset_manager.data.schemas.base import (
    BaseMongoModel,
    CreateBaseMongoModel,
    PydanticObjectId,
)


class DeveloperMongo(BaseMongoModel):
    fullname: str
    active: bool = True
    assets: List[Union[PydanticObjectId, str]] = []
    licenses: List[Union[PydanticObjectId, str]] = []


class CreateDeveloperMongo(CreateBaseMongoModel):
    fullname: str
    active: bool = True
