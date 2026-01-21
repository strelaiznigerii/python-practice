import asyncio
import random

async def get_data(i: int) -> None:
    await asyncio.sleep(random.uniform(0.1, 1))
    return f"Data from task {i}"
async def main() -> None:
    tasks = [get_data(i) for i in range(1, 11)]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
