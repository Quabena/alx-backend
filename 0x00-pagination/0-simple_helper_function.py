#!/usr/bin/env python3
"""
This module provides a helper function for pagination.
The index_range function calculates the start and end
indexes for a given page and page size.
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page sizes.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end index.
    """
    start: int = (page - 1) * page_size
    end: int = page * page_size
    return start, end
