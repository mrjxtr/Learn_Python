import asyncio  # Python standard library for async programming


async def async_task(name: str, delay: int):
    """Simulates an asynchronous task with a delay."""
    print(f"Async task '{name}' started.")
    await asyncio.sleep(delay)
    print(f"Async task '{name}' completed.")


async def main():
    """Main coroutine to execute multiple asynchronous tasks concurrently."""
    tasks = [
        async_task("Task 1", 5),
        async_task("Task 2", 2),
        async_task("Task 3", 8),
    ]
    await asyncio.gather(*tasks)
    print("All tasks completed!")


if __name__ == "__main__":
    asyncio.run(main())
