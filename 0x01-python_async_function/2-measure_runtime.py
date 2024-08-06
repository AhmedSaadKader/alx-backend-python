#!/usr/bin/env python3
"""2-Measure the runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measure the runtime of wait_n using the parameters"""
    s = time()
    await wait_n(n, max_delay)
    elapsed = time() - s
    return elapsed / n
