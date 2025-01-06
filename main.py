import asyncio
from nasdaq_client.client import NasdaqClient


async def main():
    async with NasdaqClient() as client:
        sec_filings = await client.get_sec_filings("GOOG")
        print(sec_filings)


if __name__ == "__main__":
    asyncio.run(main())
