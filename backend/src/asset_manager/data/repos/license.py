from pymongo.database import Database
from asset_manager.data.repos.base import MongoRepository
from asset_manager.data.schemas.license import LicenseMongo


class LicenseRepository(MongoRepository[LicenseMongo]):
    def __init__(self, db: Database):
        super().__init__(db, "licenses", LicenseMongo)
