#!/usr/bin/env python3
"""Pagination helper functions."""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple containing the start index and end index
    for the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
