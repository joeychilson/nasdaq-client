from typing import List, Literal, Optional, Union

from pydantic import BaseModel

from .base import Response


class KeyStatItem(BaseModel):
    label: str
    value: str


class PrimaryData(BaseModel):
    lastSalePrice: str
    netChange: str
    percentageChange: str
    deltaIndicator: str
    lastTradeTimestamp: str
    isRealTime: bool
    bidPrice: str
    askPrice: str
    bidSize: str
    askSize: str
    volume: str
    currency: Optional[str]


class UrlInfo(BaseModel):
    label: str
    value: str


class EventType(BaseModel):
    message: str
    eventName: str
    url: Optional[UrlInfo]
    id: str


class Notification(BaseModel):
    headline: str
    eventTypes: List[EventType]


class StockKeyStats(BaseModel):
    fiftyTwoWeekHighLow: KeyStatItem
    dayrange: KeyStatItem


class IndexKeyStats(BaseModel):
    previousclose: KeyStatItem
    dayrange: KeyStatItem


class Quote(BaseModel):
    symbol: str
    companyName: str
    stockType: str
    exchange: str
    isNasdaqListed: bool
    isNasdaq100: bool
    isHeld: bool
    primaryData: PrimaryData
    secondaryData: Optional[dict] = None
    marketStatus: str
    notifications: Optional[List[Notification]] = None


class StockQuote(Quote):
    assetClass: Literal["STOCKS"]
    keyStats: StockKeyStats


class IndexQuote(Quote):
    assetClass: Literal["INDEX"]
    keyStats: IndexKeyStats


QuoteResponse = Response[Union[StockQuote, IndexQuote]]
