from httpx import AsyncClient, HTTPError, Response

from nasdaq_client.models import SecFilings

DEFAULT_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


class NasdaqError(Exception):
    pass


class NasdaqClient:
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

    async def _get(self, url: str) -> Response:
        try:
            response = await self.client.get(url)
            response.raise_for_status()
            return response
        except HTTPError as e:
            raise NasdaqError(f"HTTP error occurred: {str(e)}") from e

    async def get_sec_filings(
        self,
        symbol: str,
        limit: int = 14,
        sort_column: str = "filed",
        sort_order: str = "desc",
        is_quote_media: bool = True,
    ) -> SecFilings:
        url = f"{self.base_url}/company/{symbol}/sec-filings?limit={limit}&sortColumn={sort_column}&sortOrder={sort_order}&isQuoteMedia={str(is_quote_media).lower()}"
        response = await self._get(url)
        return SecFilings.model_validate(response.json())
