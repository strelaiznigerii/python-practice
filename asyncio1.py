import asyncio

async def cook(name: str, time: int) -> None:
    print(f"{name} started")
    await asyncio.sleep(time)
    print(f"{name} finished")

tasks = [
        cook("Fry", 2),
        cook("Boil", 1),
        cook("Bake", 3)
        ]

async def main() -> None:
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
