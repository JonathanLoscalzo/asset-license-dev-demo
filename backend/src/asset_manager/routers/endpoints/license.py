from typing import List
from fastapi import APIRouter, Depends, HTTPException
from asset_manager.data.exceptions import ItemNotFound
from asset_manager.data.repos.license import LicenseRepository
from asset_manager.deps import get_current_user, get_license_repository
from asset_manager.models.auth import LoginUser

from asset_manager.models.models import License, uid

router = APIRouter(
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[License])
async def get_licenses(
    repo: LicenseRepository = Depends(get_license_repository),
    _: LoginUser = Depends(get_current_user),
) -> List[License]:
    return list(map(License.from_orm, repo.get_all()))


@router.get("/{id}", response_model=License)
async def get_license(
    id: uid,
    repo: LicenseRepository = Depends(get_license_repository),
    _: LoginUser = Depends(get_current_user),
) -> License:
    # TODO: add services/useCase and middleware
    try:
        asset = License.from_orm(repo.get(id))
        return asset
    except ItemNotFound as e:
        raise HTTPException(status_code=404, detail="Item not found") from e
