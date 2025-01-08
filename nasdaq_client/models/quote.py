from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field

from .base import Response


class KeyStatItem(BaseModel):
    label: str
    value: str


class PrimaryData(BaseModel):
    last_sale_price: str = Field(..., alias="lastSalePrice")
    net_change: str = Field(..., alias="netChange")
    percentage_change: str = Field(..., alias="percentageChange")
    delta_indicator: str = Field(..., alias="deltaIndicator")
    last_trade_timestamp: str = Field(..., alias="lastTradeTimestamp")
    is_real_time: bool = Field(..., alias="isRealTime")
    bid_price: str = Field(..., alias="bidPrice")
    ask_price: str = Field(..., alias="askPrice")
    bid_size: str = Field(..., alias="bidSize")
    ask_size: str = Field(..., alias="askSize")
    volume: str = Field(..., alias="volume")
    currency: Optional[str] = Field(None, alias="currency")


class UrlInfo(BaseModel):
    label: str
    value: str


class EventType(BaseModel):
    message: str
    event_name: str = Field(..., alias="eventName")
    url: Optional[UrlInfo]
    id: str


class Notification(BaseModel):
    headline: str
    event_types: List[EventType] = Field(..., alias="eventTypes")


class StockKeyStats(BaseModel):
    fifty_two_week_high_low: KeyStatItem = Field(..., alias="fiftyTwoWeekHighLow")
    day_range: KeyStatItem = Field(..., alias="dayrange")


class IndexKeyStats(BaseModel):
    previous_close: KeyStatItem = Field(..., alias="previousclose")
    day_range: KeyStatItem = Field(..., alias="dayrange")


class Quote(BaseModel):
    symbol: str
    company_name: str = Field(..., alias="companyName")
    stock_type: str = Field(..., alias="stockType")
    exchange: str
    is_nasdaq_listed: bool = Field(..., alias="isNasdaqListed")
    is_nasdaq_100: bool = Field(..., alias="isNasdaq100")
    is_held: bool = Field(..., alias="isHeld")
    primary_data: PrimaryData = Field(..., alias="primaryData")
    secondary_data: Optional[dict] = Field(None, alias="secondaryData")
    market_status: str = Field(..., alias="marketStatus")
    notifications: Optional[List[Notification]] = Field(None, alias="notifications")


class StockQuote(Quote):
    asset_class: Literal["STOCKS"] = Field(..., alias="assetClass")
    key_stats: StockKeyStats = Field(..., alias="keyStats")


class IndexQuote(Quote):
    asset_class: Literal["INDEX"] = Field(..., alias="assetClass")
    key_stats: IndexKeyStats = Field(..., alias="keyStats")


QuoteResponse = Response[Union[StockQuote, IndexQuote]]
