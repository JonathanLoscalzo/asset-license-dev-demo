from typing import List
from fastapi import APIRouter, Depends
from asset_manager.deps import get_current_user

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
async def get_developers():
    pass


@router.post("/", response_model=Developer)
async def add_developer(developer: CreateDev):
    pass


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
