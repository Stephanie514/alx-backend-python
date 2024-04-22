#!/usr/bin/env python3
import asyncio
from typing import List
from random import uniform
from asyncio import gather


async def wait_random(max_delay: int = 10) -> float:
    """writes an async routine called wait_n that takes in 2 int
    arguments (in this order): n and max_delay"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = [wait_random(max_delay) for _ in range(n)]
    return sorted(await gather(*delays))
