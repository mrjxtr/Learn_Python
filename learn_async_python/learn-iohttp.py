import asyncio  # Python standard library for async programming

import aiohttp  # Asynchronous HTTP client (install with pip)


async def fetch_url(url):
    """Fetches the content of a given URL asynchronously."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Fetched {url} with status {response.status}")
            return data


async def main():
    """Main coroutine to fetch multiple URLs concurrently."""
    # TODO: Dynamically generate or fetch the list of URLs
    urls = [
        "https://www.example_url1.com",
        "https://www.example_url2.com",
    ]
    # Fetch URLs concurrently
    tasks = [fetch_url(url) for url in urls]
    await asyncio.gather(*tasks)
    print("All URLs fetched!")


if __name__ == "__main__":
    asyncio.run(main())
