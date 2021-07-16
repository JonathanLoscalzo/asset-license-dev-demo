from typing import List
from fastapi import APIRouter, Depends, HTTPException
from asset_manager.data.repos.assets import AssetRepository
from asset_manager.data.repos.exceptions import ItemNotFound
from asset_manager.deps import get_asset_repository, get_current_user
from asset_manager.models.auth import LoginUser

from asset_manager.models.models import Asset, uid

router = APIRouter(
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[Asset],
)
async def get_assets(
    current_user: LoginUser = Depends(get_current_user),
    repo: AssetRepository = Depends(get_asset_repository),
) -> List[Asset]:
    return repo.get_all()


@router.get("/{id}", response_model=Asset)
async def get_asset(
    id: uid,
    repo: AssetRepository = Depends(get_asset_repository),
    _: LoginUser = Depends(get_current_user),
) -> Asset:
    # TODO: add services and middleware
    try:
        asset = repo.get(id)
        return asset
    except ItemNotFound as e:
        raise HTTPException(status_code=404, detail="Item not found") from e
