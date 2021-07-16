import uvicorn
from fastapi import FastAPI

from asset_manager.routers.api_v1 import router as router_v1
from asset_manager.routers.auth import router as auth_router

app = FastAPI(
    title="ACME Project",
)

app.include_router(router=auth_router, prefix="/auth")
app.include_router(router=router_v1, prefix="/api/v1")


def start() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start()
