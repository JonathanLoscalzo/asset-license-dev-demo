from typing import List, Optional

from asset_manager.data.schemas.base import BaseMongoModel, PydanticObjectId

class DeveloperMongo(BaseMongoModel):
    _id: PydanticObjectId
    fullname: str
    active: bool = True
    assets: List[PydanticObjectId] = []
    licenses: List[PydanticObjectId] = []

class CreateDeveloperMongo(DeveloperMongo):
    _id: Optional[PydanticObjectId]
