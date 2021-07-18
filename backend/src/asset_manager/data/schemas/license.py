from typing import List
from asset_manager.data.schemas.base import BaseMongoModel, PydanticObjectId
from asset_manager.models.models import uid


class LicenseMongo(BaseMongoModel):
    id: uid
    software: str
    # TODO: Licenses could be many-to-many with users!
    #users: List[PydanticObjectId] = []
