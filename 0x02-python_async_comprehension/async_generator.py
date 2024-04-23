#!/usr/bin/env python3
"""
This script demonstrates the usage of asyncio to create a coroutine function
that yields random numbers asynchronously.
"""
import asyncio
import random


async def async_generator():
    """
        Coroutine function that yields random numbers asynchronously.
        This coroutine loops 10 times. In each iteration, it
        asynchronously waits for 1 second, and then yields a
        random number between 0 and 10.

        Yields:
        float: A random number between 0 and 10.
     """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
