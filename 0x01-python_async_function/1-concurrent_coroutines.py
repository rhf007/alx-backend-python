#!/usr/bin/env python3
"""
Execute multiple coroutines with async
"""
import asyncio
from typing import List
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine
    """
    lst = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    end = [await tsk for tsk in asyncio.as_completed(lst)]
    return end
