from fastapi import Depends

from asset_manager.data.repos.assets import AssetRepository
from asset_manager.data.repos.developers import DeveloperRepository
from asset_manager.data.repos.license import LicenseRepository
from asset_manager.deps import get_db

def get_asset_repository(db=Depends(get_db)):
    return AssetRepository(db)


def get_license_repository(db=Depends(get_db)):
    return LicenseRepository(db)


def get_dev_repository(db=Depends(get_db)):
    return DeveloperRepository(db)
