import asyncio
import time

class Ratelimit:

    def __init__(self, *, rate):
        self.rate = rate
        self._token = 1.0
        self._last = time.monotonic()
    
    def replenish_token(self):
        now = time.monotonic()
        tokens = now - self._last * self.rate
        self._token = min(self._token + tokens, 1.0)
        self._last = now
    
    async def get_token(self):
        self.replenish_token()
        delta = (1.0 - self._token) / self.rate
        self._token -= 1.0
        await asyncio.sleep(delta)

class RatelimitMapping:
    """
    Represents the rate limit status for different keys
    Supports asynchronous access

    Attributes
    ------------
    rate: represents the max rate of call per second
    """
    def __init__(self, *, rate):
        self.rate = rate
        self._ratelimits = {}

    async def get_token(self, key):
        if key not in self._ratelimits:
            self._ratelimits[key] = Ratelimit(rate=self.rate)
        ratelimit = self._ratelimits.get(key)
        await ratelimit.get_token()

    
