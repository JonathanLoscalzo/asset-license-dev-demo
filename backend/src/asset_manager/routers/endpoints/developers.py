from typing import List
from asset_manager.data.services.developer import DeveloperService
from asset_manager.models.auth import LoginUser
from fastapi import APIRouter, Depends
from asset_manager.deps import (
    get_current_user,
    get_developer_service,
)

from asset_manager.models.models import (
    Asset,
    CreateDev,
    Developer,
    FullDeveloper,
    License,
    uid,
)
from asset_manager.models.responses import OutputResponse

router = APIRouter(
    tags=["developers"],
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[FullDeveloper])
async def get_developers(
    current_user: LoginUser = Depends(get_current_user),
    service: DeveloperService = Depends(get_developer_service),
):
    return service.get_all()


@router.post("/", response_model=Developer)
async def add_developer(
    developer: CreateDev,
    service: DeveloperService = Depends(get_developer_service),
):
    return service.add(developer)


@router.post("/{id}/activate", response_model=OutputResponse)
async def activate(
    id: uid, service: DeveloperService = Depends(get_developer_service)
):
    return service.activate(id)


@router.post("/{id}/deactivate", response_model=OutputResponse)
async def deactivate(
    id: uid, service: DeveloperService = Depends(get_developer_service)
):
    return service.deactivate(id)


@router.get("/{id}/assets", response_model=OutputResponse[List[Asset]])
async def get_assets(
    id: uid, service: DeveloperService = Depends(get_developer_service)
):
    return service.get_assets(id)


@router.patch("/{user_id}/assets/{asset_id}")
async def add_asset(
    user_id: uid,
    asset_id: uid,
    service: DeveloperService = Depends(get_developer_service),
):
    return service.add_asset(user_id, asset_id)


@router.delete("/{user_id}/assets/{asset_id}", response_model=OutputResponse)
def remove_asset(
    user_id,
    asset_id,
    service: DeveloperService = Depends(get_developer_service),
):
    return service.remove_asset(user_id, asset_id)


@router.get("/{id}/licenses", response_model=OutputResponse[List[License]])
async def get_licenses(
    id: uid, service: DeveloperService = Depends(get_developer_service)
):
    return service.get_licenses(id)


@router.patch("/{user_id}/licenses/{license_id}")
async def add_license(
    user_id,
    license_id,
    service: DeveloperService = Depends(get_developer_service),
):
    return service.add_license(user_id, license_id)


@router.delete("/{user_id}/licenses/{license_id}")
def remove_license(
    user_id,
    license_id,
    service: DeveloperService = Depends(get_developer_service),
):
    return service.remove_license(user_id, license_id)
