#!/usr/bin/env python3
"""
Module: 3-tasks

This module provides a function to create an asyncio.Task object for
the wait_random coroutine.
"""

import asyncio
from typing import Task
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Function that takes an integer max_delay and returns an asyncio.Task
    for the wait_random coroutine.

    Parameters:
        max_delay (int): Maximum delay value.

    Returns:
        Task: An asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
