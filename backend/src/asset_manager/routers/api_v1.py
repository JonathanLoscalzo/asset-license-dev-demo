from fastapi.routing import APIRouter
from asset_manager.routers.endpoints.license import router as license_router
from asset_manager.routers.endpoints.developers import router as devs_router
from asset_manager.routers.endpoints.assets import router as assets_router

router = APIRouter()

router.include_router(license_router, prefix="/licenses", tags=["licenses"])
router.include_router(assets_router, prefix="/assets", tags=["assets"])
router.include_router(assets_router, prefix="/resources", tags=["resources"])
router.include_router(devs_router, prefix="/developers", tags=["developers"])
