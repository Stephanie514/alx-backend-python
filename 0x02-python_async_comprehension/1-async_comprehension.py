#!/usr/bin/env python3
"""
This script demonstrates the usage of asyncio to create coroutines for
generating and collecting random numbers asynchronously.
"""

import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine function that collects 10 random numbers asynchronously using
    async comprehensions.This coroutine uses an async comprehension over
    async_generator to collect 10 random numbers.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    random_nos = [random_no async for random_no in async_generator()]
    return random_nos
