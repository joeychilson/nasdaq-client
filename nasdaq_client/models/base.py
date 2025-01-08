from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class Status(BaseModel):
    rCode: int
    bCodeMessage: Optional[str] = None
    developerMessage: Optional[str] = None


class Response(BaseModel, Generic[T]):
    data: T
    message: Optional[str] = None
    status: Status
