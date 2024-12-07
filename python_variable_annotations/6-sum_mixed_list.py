#!/usr/bin/env python3
"""Complex types"""
import typing


def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    """
    Mixed list
    """
    return sum(mxd_list)
