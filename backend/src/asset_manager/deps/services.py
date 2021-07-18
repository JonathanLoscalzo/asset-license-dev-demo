from fastapi import Depends
from asset_manager.data.repos.assets import AssetRepository

from asset_manager.data.repos.developers import DeveloperRepository
from asset_manager.data.repos.license import LicenseRepository
from asset_manager.data.services.developer import DeveloperService
from asset_manager.deps.repositories import (
    get_asset_repository,
    get_license_repository,
    get_dev_repository
)


def get_developer_service(
    repository: DeveloperRepository = Depends(get_dev_repository),
    asset_repo: AssetRepository = Depends(get_asset_repository),
    license_repo: LicenseRepository = Depends(get_license_repository),
):
    return DeveloperService(repository, asset_repo, license_repo)
