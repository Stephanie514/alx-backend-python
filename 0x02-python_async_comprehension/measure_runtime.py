#!/usr/bin/env python3
"""
This script measures the total runtime of executing async_comprehension four
times in parallel using asyncio.gather.
"""
import asyncio
from typing import List
from time import perf_counter


from 1_async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine function that measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = perf_counter()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime


async def main():
    return await measure_runtime()

print(asyncio.run(main()))
