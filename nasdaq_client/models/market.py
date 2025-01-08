from pydantic import BaseModel, Field

from .base import Response


class MarketData(BaseModel):
    country: str
    market_indicator: str = Field(..., alias="marketIndicator")
    ui_market_indicator: str = Field(..., alias="uiMarketIndicator")
    market_count_down: str = Field(..., alias="marketCountDown")
    pre_market_opening_time: str = Field(..., alias="preMarketOpeningTime")
    pre_market_closing_time: str = Field(..., alias="preMarketClosingTime")
    market_opening_time: str = Field(..., alias="marketOpeningTime")
    market_closing_time: str = Field(..., alias="marketClosingTime")
    after_hours_market_opening_time: str = Field(..., alias="afterHoursMarketOpeningTime")
    after_hours_market_closing_time: str = Field(..., alias="afterHoursMarketClosingTime")
    previous_trade_date: str = Field(..., alias="previousTradeDate")
    next_trade_date: str = Field(..., alias="nextTradeDate")
    is_business_day: bool = Field(..., alias="isBusinessDay")
    market_status: str = Field(..., alias="mrktStatus")
    market_count_down: str = Field(..., alias="mrktCountDown")


MarketInfoResponse = Response[MarketData]
