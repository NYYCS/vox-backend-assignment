import aiohttp
import asyncio
import time
import unittest

TOTAL_REQUESTS = 20
ERROR_MARGIN = 0.5
PAYLOAD = {
  "sender": "+393201234567",
  "receiver": "+12021234567",
  "text": "Hi Vox!"
}

async def get_total_request_time():
    async with aiohttp.ClientSession() as session:

        async def task(): 
            await session.post('http://127.0.0.1:8000/api/v1/hooli/message/', json=PAYLOAD)

        tasks = [ task() for _ in range(TOTAL_REQUESTS) ]

        start = time.monotonic()
        await asyncio.gather(*tasks)
        now = time.monotonic()
        delta = now - start

        return delta

class Test(unittest.IsolatedAsyncioTestCase):

    async def test_ratelimit(self):
        time = await get_total_request_time()
        self.assertTrue(time > TOTAL_REQUESTS - 1 - ERROR_MARGIN)
        

if __name__ == '__main__':
   unittest.main()