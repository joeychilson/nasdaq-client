from typing import List
from pydantic import BaseModel, Field
from datetime import datetime

from .base import Response


class DividendHeaders(BaseModel):
    symbol: str
    company_name: str = Field(..., alias="companyName")
    dividend_ex_date: str = Field(..., alias="dividend_Ex_Date")
    payment_date: str = Field(..., alias="payment_Date")
    record_date: str = Field(..., alias="record_Date")
    dividend_rate: str = Field(..., alias="dividend_Rate")
    indicated_annual_dividend: str = Field(..., alias="indicated_Annual_Dividend")
    announcement_date: str = Field(..., alias="announcement_Date")


class DividendRow(BaseModel):
    company_name: str = Field(..., alias="companyName")
    symbol: str
    dividend_ex_date: str = Field(..., alias="dividend_Ex_Date")
    payment_date: str = Field(..., alias="payment_Date")
    record_date: str = Field(..., alias="record_Date")
    dividend_rate: float = Field(..., alias="dividend_Rate")
    indicated_annual_dividend: float = Field(..., alias="indicated_Annual_Dividend")
    announcement_date: str = Field(..., alias="announcement_Date")


class TimeFrame(BaseModel):
    min_date: datetime = Field(..., alias="minDate")
    max_date: datetime = Field(..., alias="maxDate")


class Calendar(BaseModel):
    as_of: str = Field(..., alias="asOf")
    headers: DividendHeaders
    rows: List[DividendRow]


class DividendData(BaseModel):
    calendar: Calendar
    timeframe: TimeFrame


DividendCalendarResponse = Response[DividendData]
