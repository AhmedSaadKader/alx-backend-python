#!/usr/bin/env python3
"""0. The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that takes in an integer argument
    [max_delay] with a default value of 10 and waits for a random
    delay between 0 and [max_delay] and eventually returns it"""
    random_delay = random.triangular(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
