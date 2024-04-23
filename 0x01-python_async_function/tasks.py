#!/usr/bin/env python3
"""
Module: task_wait_random

This module provides a function to create an asyncio.Task object that waits for a random delay between 0 and max_delay.

Functions:
    task_wait_random(max_delay: int) -> asyncio.Task: Create an asyncio.Task that waits for a random delay.
"""

import asyncio
from typing import Callable
from asyncio import Task
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> Task:
    """
    Create an asyncio.Task that waits for a random delay between 0 and max_delay.
    
    Parameters:
        max_delay (int): Maximum delay value.
        
    Returns:
        asyncio.Task: Task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
