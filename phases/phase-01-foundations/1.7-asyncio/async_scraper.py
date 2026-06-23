import asyncio
import aiohttp
import json
from pydantic import BaseModel
from datetime import datetime

class APIResponse(BaseModel):
    id: int           # matches the API field name
    name: str
    email: str

async def fetch_data(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return APIResponse(**data)

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/users/1",
        "https://jsonplaceholder.typicode.com/users/2",
        "https://jsonplaceholder.typicode.com/users/3"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    with open("async_results.json", "w") as f:
        json.dump([r.model_dump() for r in results], f, indent=2)

    print(f"Fetched {len(results)} records at {datetime.now()}")
    for r in results:
        print(r)

if __name__ == "__main__":
    asyncio.run(main())
