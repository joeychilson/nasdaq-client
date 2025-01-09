from typing import List
from pydantic import BaseModel, Field
from datetime import datetime

from .base import Response


class CalendarHeaders(BaseModel):
    symbol: str
    company_name: str = Field(..., alias="companyName")
    dividend_ex_date: str = Field(..., alias="dividend_Ex_Date")
    payment_date: str = Field(..., alias="payment_Date")
    record_date: str = Field(..., alias="record_Date")
    dividend_rate: str = Field(..., alias="dividend_Rate")
    indicated_annual_dividend: str = Field(..., alias="indicated_Annual_Dividend")
    announcement_date: str = Field(..., alias="announcement_Date")


class CalendarRow(BaseModel):
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
    headers: CalendarHeaders
    rows: List[CalendarRow]


class DividendCalendar(BaseModel):
    calendar: Calendar
    timeframe: TimeFrame


DividendCalendarResponse = Response[DividendCalendar]
