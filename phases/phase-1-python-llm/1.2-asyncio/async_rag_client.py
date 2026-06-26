import asyncio
import time
import httpx
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


async def fetch_user(client: httpx.AsyncClient, user_id: int) -> User:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = await client.get(url)
    response.raise_for_status()
    return User(**response.json())


async def main():
    async with httpx.AsyncClient() as client:
        # Concurrent
        start = time.perf_counter()
        tasks = [fetch_user(client, i) for i in range(1, 4)]
        results = await asyncio.gather(*tasks)
        concurrent_time = time.perf_counter() - start
        print(f"Concurrent: {concurrent_time:.3f}s")
        for user in results:
            print(user)

        # Sequential
        start = time.perf_counter()
        for i in range(1, 4):
            user = await fetch_user(client, i)
        sequential_time = time.perf_counter() - start
        print(f"Sequential: {sequential_time:.3f}s")
        print(f"Speedup: {sequential_time / concurrent_time:.2f}x")


if __name__ == "__main__":
    asyncio.run(main())
