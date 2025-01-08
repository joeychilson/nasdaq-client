from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class Status(BaseModel):
    return_code: int = Field(..., alias="rCode")
    return_message: Optional[str] = Field(None, alias="bCodeMessage")
    developer_message: Optional[str] = Field(None, alias="developerMessage")


class Response(BaseModel, Generic[T]):
    data: T
    message: Optional[str] = None
    status: Status
