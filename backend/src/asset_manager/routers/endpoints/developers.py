from typing import List
from asset_manager.data.repos.developers import DeveloperRepository
from asset_manager.data.services.developer import DeveloperService
from asset_manager.models.auth import LoginUser
from fastapi import APIRouter, Depends
from asset_manager.deps import get_asset_repository, get_current_user, get_developer_service

from asset_manager.models.models import (
    Asset,
    CreateDev,
    Developer,
    FullDeveloper,
    uid,
)

router = APIRouter(
    tags=["developers"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[FullDeveloper])
async def get_developers(
    current_user: LoginUser = Depends(get_current_user),
    repo: DeveloperRepository = Depends(get_asset_repository),
):
    devs = repo.get_all()

    return devs


@router.post("/", response_model=Developer)
async def add_developer(
    developer: CreateDev,
    service: DeveloperService = Depends(get_developer_service),
):
    return service.add(developer)
    


@router.post("/{id}/activate")
async def activate(id: uid):
    pass


@router.post("/{id}/deactivate")
async def deactivate(id: uid):
    pass


@router.get("/{id}/assets", response_model=List[Asset])
async def get_assets(id: uid):
    pass


@router.patch("/{user_id}/assets/{asset_id}")
async def add_asset(user_id: uid, asset_id: uid):
    pass


@router.delete("/{user_id}/assets/{asset_id}")
def remove_asset(user_id, asset_id):
    pass


@router.get("/{id}/licenses", response_model=List[Asset])
async def get_licenses(id: uid):
    pass


@router.patch("/{user_id}/licenses/{license_id}")
async def add_license(user_id, license_id):
    pass


@router.delete("/{user_id}/licenses/{license_id}")
def remove_license(user_id, license_id):
    pass
