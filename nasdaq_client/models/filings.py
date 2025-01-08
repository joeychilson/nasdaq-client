from typing import List

from pydantic import BaseModel, Field

from .base import Response


class LatestItem(BaseModel):
    label: str
    value: str


class Headers(BaseModel):
    company_name: str = Field(..., alias="companyName")
    form_type: str = Field(..., alias="formType")
    filed: str
    period: str
    view: str


class FilterOption(BaseModel):
    group: str
    form_type: List[str] = Field(..., alias="formtype")


class View(BaseModel):
    html_link: str = Field(..., alias="htmlLink")
    doc_link: str = Field(..., alias="docLink")
    pdf_link: str = Field(..., alias="pdfLink")
    xbr_link: str = Field(..., alias="xbrLink")
    ixbrl_content: str = Field(..., alias="ixbrlContent")
    xls_link: str = Field(..., alias="xlsLink")
    xbrl_sub_doc: str = Field(..., alias="xBrlSubDoc")


class Row(BaseModel):
    company_name: str = Field(..., alias="companyName")
    reporting_owner: str = Field(..., alias="reportingOwner")
    form_type: str = Field(..., alias="formType")
    filed: str
    period: str
    view: View


class FilingsData(BaseModel):
    symbol: str
    total_records: int = Field(..., alias="totalRecords")
    latest: List[LatestItem]
    headers: Headers
    filter_options: List[FilterOption] = Field(..., alias="filterOptions")
    rows: List[Row]


FilingsResponse = Response[FilingsData]
