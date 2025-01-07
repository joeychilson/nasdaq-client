import asyncio
from nasdaq_client.client import NasdaqClient


async def main():
    async with NasdaqClient() as client:
        index_data = await client.get_quote_info("COMP", asset_class="index")
        print(index_data)

        stock_data = await client.get_quote_info("GOOG")
        print(stock_data)


if __name__ == "__main__":
    asyncio.run(main())
