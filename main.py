import asyncio

from nasdaq_client import NasdaqClient


async def main():
    async with NasdaqClient() as client:
        index_data = await client.get_quote("COMP", asset_class="index")
        print(index_data)

        stock_data = await client.get_quote("GOOG")
        print(stock_data)

        market_data = await client.get_market_info()
        print(market_data)


if __name__ == "__main__":
    asyncio.run(main())
