from enum import Enum
from pydantic import BaseModel
from typing import Union, Optional, List
from uuid import UUID

from asset_manager.data.schemas.developer import DeveloperMongo

uid = Union[str, int, UUID]


class TypeAssetEnum(str, Enum):
    laptop = "laptop"
    keyboard = "keyboard"
    mouse = "mouse"
    headset = "headset"
    monitor = "monitor"


class CreateDev(BaseModel):
    fullname: str
    active: bool = True


class Developer(CreateDev, BaseModel):
    id: uid

    # class Config:
    #     orm_mode = True


class License(BaseModel):
    id: uid
    software: str
    users: List[Union[Developer, uid]] = []

    class Config:
        orm_mode = True


class Asset(BaseModel):
    id: uid
    brand: str
    model: str
    type: TypeAssetEnum
    user: Optional[Union[Developer, uid]]

    class Config:
        orm_mode = True


class FullDeveloper(Developer):
    assets: List[Union[Asset, uid]] = []
    licenses: List[Union[License, uid]] = []

    def create_model_from_devmongo(
        dev: DeveloperMongo,
    ):
        return FullDeveloper(
            id=str(dev.id),
            fullname=dev.fullname,
            active=dev.active,
            licenses=dev.licenses,
            assets=dev.assets,
        )
