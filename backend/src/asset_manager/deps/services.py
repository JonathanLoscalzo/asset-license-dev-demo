from fastapi import Depends

from asset_manager.data.repos.developers import DeveloperRepository
from asset_manager.data.services.developer import DeveloperService
from asset_manager.deps import get_dev_repository


def get_developer_service(
    repository: DeveloperRepository = Depends(get_dev_repository),
):
    return DeveloperService(repository)
