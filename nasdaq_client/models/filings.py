from typing import List

from pydantic import BaseModel

from .base import Response


class LatestItem(BaseModel):
    label: str
    value: str


class Headers(BaseModel):
    companyName: str
    formType: str
    filed: str
    period: str
    view: str


class FilterOption(BaseModel):
    group: str
    formtype: List[str]


class View(BaseModel):
    htmlLink: str
    docLink: str
    pdfLink: str
    xbrLink: str
    ixbrlContent: str
    xlsLink: str
    xBrlSubDoc: str


class Row(BaseModel):
    companyName: str
    reportingOwner: str
    formType: str
    filed: str
    period: str
    view: View


class FilingsData(BaseModel):
    symbol: str
    totalRecords: int
    latest: List[LatestItem]
    headers: Headers
    filterOptions: List[FilterOption]
    rows: List[Row]


FilingsResponse = Response[FilingsData]
