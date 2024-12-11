#!/usr/bin/env python3
"""[Pagination]"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Berk Pagination
    """
    start = (page-1) * page_size
    end = start + page_size
    return start, end
