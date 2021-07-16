from typing import Optional

from asset_manager.data.schemas.base import BaseMongoModel, PydanticObjectId

from asset_manager.models.models import TypeAssetEnum, uid


class AssetMongo(BaseMongoModel):
    id: uid
    brand: str
    model: str
    type: TypeAssetEnum
    user: Optional[PydanticObjectId]
