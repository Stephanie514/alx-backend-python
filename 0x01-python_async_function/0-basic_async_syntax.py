#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument (max_delay)
    and waits for a random delay between 0 and max_delay (inclusive).

    Parameters:
        max_delay (int): Maximum delay value (default is 10).

    Returns:
        float: Random delay value.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
