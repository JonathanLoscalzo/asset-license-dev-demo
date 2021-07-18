from fastapi.params import Depends
from pymongo.collection import ReturnDocument
from asset_manager.data.exceptions.base import ItemNotFound
from asset_manager.data.repos.assets import AssetRepository
from asset_manager.data.repos.developers import DeveloperRepository
from asset_manager.data.repos.license import LicenseRepository
from asset_manager.data.schemas.developer import (
    CreateDeveloperMongo,
    DeveloperMongo,
)
from bson import ObjectId
from asset_manager.models.models import CreateDev, Developer


class DeveloperService:
    __repository: DeveloperRepository

    def __init__(
        self,
        repository: DeveloperRepository = Depends(),
        asset_repo: AssetRepository = Depends(),
        license_repo: LicenseRepository = Depends(),
    ):
        self.__repository = repository

    def add(self, create_dev: CreateDev) -> Developer:
        devMongo = CreateDeveloperMongo.parse_obj(create_dev)
        _id = self.__repository.add(devMongo)
        return Developer(id=str(_id), **create_dev.dict())

    def _change_active_user(self, uid, active:bool):
        res = self.__repository.collection().find_one_and_update(
            {"_id": ObjectId(uid)},
            {"$set": {"active": active}},
            return_document=ReturnDocument.AFTER,
        )

        if res is None: 
            raise ItemNotFound(uid)

        return active

    def activate(self, uid):
        return self._change_active_user(uid, True)

    def deactivate(self, uid):
        return self._change_active_user(uid, True)

    def add_asset(self, developer_id, asset_id):
        pass

    def add_license(self, developer_id, asset_id):
        pass
