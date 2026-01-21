import asyncio
import random

async def fake_request(i: int):
    print(f"📡 Запрос {i} отправлен")
    await asyncio.sleep(random.uniform(0.5, 1.5))
    print(f"✅ Ответ {i} получен")

async def main():
    tasks = [fake_request(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)

asyncio.run(main())

