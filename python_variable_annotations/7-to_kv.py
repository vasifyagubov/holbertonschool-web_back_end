#!/usr/bin/env python3
"""Complex types"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    String and float
    """
    return (k, v**2)
