#!/usr/bin/env python3
"""
Async Comprehensions
"""
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """
    yield random numbers collected
    """
    stop = [i async for i in async_generator()]
    return stop
