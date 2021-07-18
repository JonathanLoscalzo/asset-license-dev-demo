from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from asset_manager.data.exceptions.base import ItemNotFound

def add_exceptions_handlers(app: FastAPI):
    @app.exception_handler(ItemNotFound)
    def itemnotfound_handler(request: Request, exc: ItemNotFound):
        return JSONResponse(status_code=404, content={"message": exc.message})
