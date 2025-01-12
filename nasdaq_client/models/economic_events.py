from pydantic import BaseModel, Field

from .base import Response


class EconomicEventHeaders(BaseModel):
    time: str = Field(..., alias="gmt")
    country: str
    event_name: str = Field(..., alias="eventName")
    actual: str
    consensus: str
    previous: str
    description: str


class EconomicEventRow(BaseModel):
    time: str = Field(..., alias="gmt")
    country: str
    event_name: str = Field(..., alias="eventName")
    actual: str
    consensus: str
    previous: str
    description: str


class EconomicEventsData(BaseModel):
    as_of: str = Field(..., alias="asOf")
    headers: EconomicEventHeaders
    rows: list[EconomicEventRow]


EconomicEventsResponse = Response[EconomicEventsData]
