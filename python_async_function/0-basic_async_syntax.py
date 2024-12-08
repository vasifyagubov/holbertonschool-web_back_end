#!/usr/bin/env python3
"""Basic async syntax."""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random amount of seconds."""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
