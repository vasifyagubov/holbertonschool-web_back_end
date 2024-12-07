#!/usr/bin/env python3
"""Lets Duck Type"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
                        typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Iterable Object
    """
    return [(i, len(i)) for i in lst]
