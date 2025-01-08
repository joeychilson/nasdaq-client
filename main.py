import asyncio

from nasdaq_client import NasdaqClient


async def main():
    async with NasdaqClient() as client:
        filings_data = await client.get_sec_filings("GOOG")
        print(filings_data)

        index_data = await client.get_quote_info("COMP", asset_class="index")
        print(index_data)

        stock_data = await client.get_quote_info("GOOG")
        print(stock_data)

        market_data = await client.get_market_info()
        print(market_data)


if __name__ == "__main__":
    asyncio.run(main())
