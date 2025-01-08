import asyncio

from rich import print

from nasdaq_client import NasdaqClient


async def main():
    async with NasdaqClient() as client:
        dividend_data = await client.get_dividend_calendar("2025-01-07")
        print(dividend_data)


if __name__ == "__main__":
    asyncio.run(main())
