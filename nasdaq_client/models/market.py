from pydantic import BaseModel

from .base import Response


class MarketData(BaseModel):
    country: str
    marketIndicator: str
    uiMarketIndicator: str
    marketCountDown: str
    preMarketOpeningTime: str
    preMarketClosingTime: str
    marketOpeningTime: str
    marketClosingTime: str
    afterHoursMarketOpeningTime: str
    afterHoursMarketClosingTime: str
    previousTradeDate: str
    nextTradeDate: str
    isBusinessDay: bool
    mrktStatus: str
    mrktCountDown: str


MarketInfoResponse = Response[MarketData]
