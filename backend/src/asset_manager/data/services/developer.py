from typing import List
from asset_manager.data.exceptions.base import (
    AssetHasAssignedException,
    ItemNotFound,
    UserJustHaveAssetException,
)
from asset_manager.data.repos.assets import AssetRepository
from asset_manager.data.repos.developers import DeveloperRepository
from asset_manager.data.repos.license import LicenseRepository
from asset_manager.data.schemas.developer import (
    CreateDeveloperMongo,
    DeveloperMongo,
)
from bson import ObjectId
from asset_manager.models.models import CreateDev, Developer, FullDeveloper
from asset_manager.models.responses import ApiStatus, OutputResponse


class DeveloperService:
    __repository: DeveloperRepository

    def __init__(
        self,
        repository: DeveloperRepository,
        asset_repo: AssetRepository,
        license_repo: LicenseRepository,
    ):
        self.__repository = repository
        self._asset_repo = asset_repo
        self._license_repo = license_repo

    def get_all(self) -> List[FullDeveloper]:
        return list(
            map(
                FullDeveloper.create_model_from_devmongo,
                self.__repository.get_all(),
            )
        )

    def add(self, create_dev: CreateDev) -> Developer:
        devMongo = CreateDeveloperMongo(**create_dev.dict())
        _id = self.__repository.add(devMongo)
        return Developer(id=str(_id), **create_dev.dict())

    def _change_active_user(self, uid, active: bool):
        res = self.__repository.update(uid, {"$set": {"active": active}})

        if res is None:
            raise ItemNotFound(uid)

        return active

    def activate(self, uid):
        return self._change_active_user(uid, True)

    def deactivate(self, uid):
        return self._change_active_user(uid, False)

    def add_asset(self, developer_id, asset_id):
        """Add asset relationship to current user

        Constrains:
            - asset has just one dev
            - dev may have several assets

        Args:
            developer_id (uid): developer id (ObjectId)
            asset_id (uid): asset id (ObjectId)
        """

        asset = self._asset_repo.get(asset_id)

        if asset.user is not None:
            raise AssetHasAssignedException(asset.id)

        relationship = self.__repository.get_by_filter(
            {"_id": ObjectId(developer_id), "assets": {"$in": [asset.id]}}
        )

        if relationship:
            raise UserJustHaveAssetException(asset.user, asset.id)

        dev = self.__repository.update(
            developer_id,
            {"$push": {"assets": asset.id}},
        )

        self._asset_repo.update(
            asset.id, {"$set": {"user": ObjectId(developer_id)}}
        )

        return OutputResponse[dict](
            status=ApiStatus.ok,
            data={
                "developer": FullDeveloper.create_model_from_devmongo(
                    DeveloperMongo.parse_obj(dev)
                )
            },
            message="Updated relationship",
        )

    def add_license(self, developer_id, license_id):
        pass
