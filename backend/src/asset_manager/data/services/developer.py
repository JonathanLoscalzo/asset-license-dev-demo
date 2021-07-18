from fastapi.params import Depends
from asset_manager.data.repos.assets import AssetRepository
from asset_manager.data.repos.developers import DeveloperRepository
from asset_manager.data.repos.license import LicenseRepository
from asset_manager.data.schemas.developer import (
    CreateDeveloperMongo,
    DeveloperMongo,
)
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

    def add_asset(self, developer_id, asset_id):
        pass

    def add_license(self, developer_id, asset_id):
        pass
