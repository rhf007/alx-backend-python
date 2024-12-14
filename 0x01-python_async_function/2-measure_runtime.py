#!/usr/bin/env python3
"""total execution time"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total_timen"""
    s_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    e_time = time.perf_counter()
    return (e_time - s_time) / n
