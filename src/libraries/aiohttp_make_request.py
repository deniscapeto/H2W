import asyncio

import aiohttp


async def request(url):
    print(f'Shooting to {url}')

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.text()
            print(f'response from [{url}]: ({response.status}) {response_text[0:30]}')

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(request('https://www.deniscapeto.com'))
