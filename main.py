import asyncio

from rich import print

from nasdaq_client import NasdaqClient


async def main():
    async with NasdaqClient() as client:
        events = await client.get_economic_events("2025-01-11")
        print(events)


if __name__ == "__main__":
    asyncio.run(main())
