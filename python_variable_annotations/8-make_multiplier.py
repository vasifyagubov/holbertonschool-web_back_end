#!/usr/bin/env python3
"""Make multipler"""
import typing


def make_multipler(multiplier: float) -> typing.Callable[[float], float]:
    """
    Functions
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
