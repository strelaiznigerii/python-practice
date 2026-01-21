import asyncio
from typing import AsyncGenerator
import random

NEWS = [
    "Погода хорошая",
    "⚠️ Важно: Землетрясение в Японии",
    "Акции растут",
    "⚠️ Важно: Утечка данных пользователей",
    "Курс доллара стабильный",
]


async def stream_news() -> AsyncGenerator[str, None]:
    for _ in range(10):
        await asyncio.sleep(0.5)
        yield random.choice(NEWS)

async def main() -> None:
    async for news in stream_news():
        if "⚠️ Важно" in news:
            print(news)

asyncio.run(main())
