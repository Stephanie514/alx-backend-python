#!/usr/bin/env python3
"""
Module: 2-measure_runtime

This module provides a function to measure the total execution time for
wait_n(n, max_delay),
and returns the average time per iteration.
"""

import asyncio
from time import perf_counter
from typing import List
from concurrent_coroutines import wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n.

    Parameters:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value.

    Returns:
        float: Average execution time per operation.
    """
    start_time = perf_counter()
    await asyncio.gather(wait_n(n, max_delay))
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 3
    result = asyncio.run(measure_time(n, max_delay))
    print(result)
