#!/usr/bin/env python3
""" FIFOCache module that implements a caching system using FIFO algorithm.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that removes the oldest item in the cache
    when the maximum capacity is reached, following the FIFO eviction policy.
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance by calling the parent constructor.
        """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """
        Add an item to the cache using the specified key.
        If the cache exceeds MAX_ITEMS, remove the oldest entry (FIFO).

        Args:
            key: The key under which the item should be stored.
            item: The item to store.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.keys_order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.keys_order.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

    def get(self, key):
        """
        Retrieve an item from the cache using the specified key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
