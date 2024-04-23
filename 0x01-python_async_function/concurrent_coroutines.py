#!/usr/bin/env python3
"""
Module: 1-concurrent_coroutines

This module contains asynchronous coroutines for handling
concurrent operations.
"""

import asyncio
from typing import List
from random import uniform
from asyncio import gather


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that generates a random delay between 0 and
    max_delay (inclusive) seconds and eventually returns it.

    Parameters:
        max_delay (int): Maximum delay value (default is 10).

    Returns:
        float: Random delay value.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the
    specified max_delay and returns the list of all the delays.

    Parameters:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await gather(*delays))
