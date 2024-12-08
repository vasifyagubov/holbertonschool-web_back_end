#!/usr/bin/env python3
"""Measure the runtime of wait_n."""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total runtime and returns it."""

    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()

    return (end - start) / n
