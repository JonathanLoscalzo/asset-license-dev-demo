from fastapi import FastAPI, Request
import importlib
from fastapi.exceptions import HTTPException

# from fastapi.responses import JSONResponse
from asset_manager.data.exceptions.base import (
    AssetManagerException,
)
from fastapi.exception_handlers import http_exception_handler


def add_exceptions_handlers(app: FastAPI):

    exceptions = importlib.import_module("asset_manager.data.exceptions")

    exceptions = [
        (name, cls)
        for name, cls in exceptions.__dict__.items()
        if type(cls) is type and AssetManagerException in cls.mro()
    ]

    async def generic_handler(request: Request, exc):
        ex = HTTPException(status_code=404, detail={"message": exc.message})
        return await http_exception_handler(request, ex)

    for _name, cls in exceptions:
        app.exception_handler(cls)(generic_handler)

    # TODO: log handlers
