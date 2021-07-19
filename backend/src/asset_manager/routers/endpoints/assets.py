from typing import List
from fastapi import APIRouter, Depends, HTTPException
from asset_manager.data.repos.assets import AssetRepository
from asset_manager.data.exceptions import ItemNotFound
from asset_manager.deps import get_asset_repository, get_current_user

from asset_manager.models.models import Asset, uid

router = APIRouter(
    dependencies=[Depends(get_current_user)],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[Asset],
)
async def get_assets(
    repo: AssetRepository = Depends(get_asset_repository),
) -> List[Asset]:
    return list(map(Asset.from_orm, repo.get_all()))


@router.get("/{id}", response_model=Asset)
async def get_asset(
    id: uid,
    repo: AssetRepository = Depends(get_asset_repository),
) -> Asset:
    # TODO: add services and middleware
    try:
        asset = Asset.from_orm(repo.get(id))
        return asset
    except ItemNotFound as e:
        raise HTTPException(status_code=404, detail="Item not found") from e
