#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end index for pagination.

    Args:
        page (int): current page number (1-indexed)
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: start and end indexes for slicing
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset: List[List] = None
        self.__indexed_dataset: Dict[int, List] = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: dataset excluding the header row
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create an indexed version of the dataset.

        Returns:
            Dict[int, List]: dataset mapped by original index
        """
        if self.__indexed_dataset is None:
            full_dataset = self.dataset()
            self.__indexed_dataset = {
                i: row for i, row in enumerate(full_dataset)
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of the dataset using traditional pagination.

        Args:
            page (int): current page number (1-indexed)
            page_size (int): number of items per page

        Returns:
            List[List]: the page data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page of the dataset starting from a given index,
        resilient to deletion from the dataset.

        Args:
            index (int): the starting index
            page_size (int): number of items per page

        Returns:
            Dict: dictionary with pagination metadata and data
        """
        data = self.indexed_dataset()

        # Ensure index is valid
        assert index is not None
        assert isinstance(index, int) and index >= 0
        assert index <= max(data.keys())

        page_data: List[List] = []
        data_collected = 0
        next_index = None
        current = index

        # Collect items starting from `index`, skipping missing entries
        while data_collected < page_size and current <= max(data.keys()):
            item = data.get(current)
            if item:
                page_data.append(item)
                data_collected += 1
            current += 1

        # Determine the next index (i.e., where the next page should start)
        while current <= max(data.keys()):
            if data.get(current):
                next_index = current
                break
            current += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_data),
            'data': page_data,
        }
