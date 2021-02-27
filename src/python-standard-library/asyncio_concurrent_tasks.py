import asyncio
import random
from asyncio.tasks import Task
from typing import List


class Requester:

    def __init__(self, url) -> None:
        self.url = url
        pass

    async def make(self):
        await asyncio.sleep(random.randint(1, 5))
        print(f'(faking) Shooting to {self.url}')


if __name__ == "__main__":

    requesters: List[Requester] = [
        Requester('http://www.google.com'),
        Requester('http://www.microsoft.com')
    ]

    tasks: List[Task] = []
    for requester in requesters:
        tasks.append(
            requester.make()
        )

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait(tasks))
