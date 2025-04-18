from httpx import AsyncClient, HTTPError, Response as HttpxResponse

from nasdaq_client.models import (
    DividendCalendarResponse,
    EconomicEventsResponse,
    MarketInfoResponse,
    QuoteInfoResponse,
    SecFilingsResponse,
)

DEFAULT_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


class NasdaqError(Exception):
    """
    An error occurred while interacting with the Nasdaq API.
    """

    pass


class NasdaqClient:
    """
    A client for the Nasdaq API.
    """

    base_url = "https://api.nasdaq.com/api"

    def __init__(
        self,
        user_agent: str = DEFAULT_USER_AGENT,
        timeout: int = 30,
    ):
        self.user_agent = user_agent
        self.timeout = timeout
        self.client = AsyncClient(
            headers={"User-Agent": self.user_agent},
            timeout=timeout,
        )

    async def __aenter__(self) -> "NasdaqClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.client.aclose()

    async def _get(self, url: str) -> HttpxResponse:
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response
        except HTTPError as e:
            raise NasdaqError(f"HTTP error occurred: {str(e)}") from e

    async def get_dividend_calendar(self, date: str) -> DividendCalendarResponse:
        """
        Get dividend calendar information for a specific date.

        Args:
            date: The date to query dividends for in YYYY-MM-DD format (e.g., '2025-01-07')

        Returns:
            DividendCalendarResponse: Dividend calendar information including company details,
                                    dividend rates, and important dates wrapped in the standard
                                    response format
        """
        url = f"{self.base_url}/calendar/dividends?date={date}"
        response = await self._get(url)
        return DividendCalendarResponse.model_validate(response.json())

    async def get_economic_events(self, date: str) -> EconomicEventsResponse:
        """
        Get economic events calendar for a specific date.

        Args:
            date: The date to query economic events for in YYYY-MM-DD format (e.g., '2025-01-11')

        Returns:
            EconomicEventsResponse: Economic events information including event details,
                                  actual/consensus/previous values, and descriptions wrapped
                                  in the standard response format
        """
        url = f"{self.base_url}/calendar/economicevents?date={date}"
        response = await self._get(url)
        return EconomicEventsResponse.model_validate(response.json())

    async def get_market_info(self) -> MarketInfoResponse:
        """
        Get current market information including trading hours and market status.

        Returns:
            MarketInfoResponse: Market information including trading hours, status,
                              and countdown wrapped in the standard response format
        """
        url = f"{self.base_url}/market-info"
        response = await self._get(url)
        return MarketInfoResponse.model_validate(response.json())

    async def get_quote_info(
        self,
        symbol: str,
        asset_class: str = "stocks",
    ) -> QuoteInfoResponse:
        """
        Get quote information for a given symbol.

        Args:
            symbol: The stock symbol or index to query (e.g., 'TSLA' or 'COMP')
            asset_class: The asset class to query ('stocks' or 'index')

        Returns:
            QuoteResponse: Quote information including price, company details, and market status
                         wrapped in the standard response format
        """
        url = f"{self.base_url}/quote/{symbol}/info?assetclass={asset_class.lower()}"
        response = await self._get(url)
        return QuoteInfoResponse.model_validate(response.json())

    async def get_sec_filings(
        self,
        symbol: str,
        limit: int = 14,
        sort_column: str = "filed",
        sort_order: str = "desc",
        is_quote_media: bool = True,
    ) -> SecFilingsResponse:
        """
        Get SEC filings for a given symbol.

        Args:
            symbol: The stock symbol to query (e.g., 'TSLA' or 'COMP')
            limit: The number of filings to return (default is 14)
            sort_column: The column to sort by (default is 'filed')
            sort_order: The order to sort by (default is 'desc')
            is_quote_media: Whether to include quote media (default is True)

        Returns:
            FilingsResponse: SEC filings including headers, rows, and data wrapped in the standard response format
        """
        url = f"{self.base_url}/company/{symbol}/sec-filings?limit={limit}&sortColumn={sort_column}&sortOrder={sort_order}&isQuoteMedia={str(is_quote_media).lower()}"
        response = await self._get(url)
        return SecFilingsResponse.model_validate(response.json())
