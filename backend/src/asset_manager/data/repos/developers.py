from asset_manager.data.schemas.developer import DeveloperMongo
from pymongo.database import Database
from asset_manager.data.repos.base import MongoRepository


class DeveloperRepository(MongoRepository[DeveloperMongo]):
    def __init__(self, db: Database):
        super().__init__(db, "developers", DeveloperMongo)
