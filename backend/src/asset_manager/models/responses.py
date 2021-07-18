from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from enum import Enum

T = TypeVar("T")


class ApiStatus(str, Enum):
    error = "error"
    ok = "ok"


class OutputResponse(GenericModel, Generic[T]):
    data: Optional[T] = None
    message: Optional[str] = None
    status: ApiStatus = ApiStatus.ok
