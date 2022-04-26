import aiohttp
import asyncio
from datetime import datetime


start_time = datetime.now()


async def parser():
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.get(input("url = ")) as resp:
                answer = await resp.json()
                print (answer)
                print(datetime.now() - start_time)


asyncio.run(parser())
