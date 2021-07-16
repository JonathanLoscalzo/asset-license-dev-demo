from enum import Enum
from pydantic import BaseModel
from typing import Union, Optional, List
from uuid import UUID

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
    user: Optional[Developer]


class Asset(BaseModel):
    id: uid
    brand: str
    model: str
    type: TypeAssetEnum
    user: Optional[Developer]


class AssetRelationship:
    assets: List[Asset] = []


class LicenseRelationship:
    licenses: List[License] = []


class FullDeveloper(
    AssetRelationship, LicenseRelationship, Developer, BaseModel
):
    pass
