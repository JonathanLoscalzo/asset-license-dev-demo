from pymongo.database import Database
from asset_manager.data.repos.base import MongoRepository
from asset_manager.data.schemas.asset import AssetMongo


class AssetRepository(MongoRepository[AssetMongo]):
    def __init__(self, db: Database):
        super().__init__(db, "assets", AssetMongo)
