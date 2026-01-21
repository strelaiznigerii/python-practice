import asyncio
import httpx

async def get_post(post_id: int) -> None:
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            data = response.json()
            print(f"[{post_id}] {data['title']}")
        except httpx.RequestError as e:
            print(f"[{post_id}] Ошибка: {e}")

async def main():
    tasks = [get_post(i) for i in range(1, 21)]
    await asyncio.gather(*tasks)

asyncio.run(main())

