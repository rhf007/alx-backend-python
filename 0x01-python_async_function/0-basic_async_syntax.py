#!/usr/bin/env python3
'''
async
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for delay ranged between 0 and max_delay (included)
    """
    dly = random.uniform(0, max_delay)
    await asyncio.sleep(dly)
    return dly
