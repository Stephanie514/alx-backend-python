#!/usr/bin/env python3
"""
Module: tasks

This module provides asynchronous coroutines for handling tasks.
"""
import asyncio
from typing import List
from random import uniform
from asyncio import gather


async def task_wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay (inclusive) seconds and eventually returns it.

    Parameters:
        max_delay (int): Maximum delay value (default is 10).

    Returns:
        float: Random delay value.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times with the
    specified max_delay and returns the list of all the delays.

    Parameters:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay value.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await gather(*delays))
