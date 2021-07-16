from typing import Optional

from asset_manager.data.schemas.base import BaseMongoModel, PydanticObjectId

from asset_manager.models.models import uid


class LicenseMongo(BaseMongoModel):
    id: uid
    software: str
    user: Optional[PydanticObjectId]
