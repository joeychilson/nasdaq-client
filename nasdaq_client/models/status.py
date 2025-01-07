from typing import Optional

from pydantic import BaseModel


class Status(BaseModel):
    rCode: int
    bCodeMessage: Optional[str]
    developerMessage: Optional[str]
