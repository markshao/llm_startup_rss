import asyncio
from a16z import A16zDataFetcher

async def main():
    df = A16zDataFetcher()
    await df.execute()

if __name__ == "__main__":
    asyncio.run(main())
