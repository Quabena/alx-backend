#!/usr/bin/env python3
""" LIFOCache module that implements a caching system using LIFO algorithm.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that removes the most recently added item
    when the maximum capacity is reached, following the LIFO eviction policy.
    """

    def __init__(self):
        """
        Initialize the LIFOCache instance by calling the parent constructor.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item to the cache using the specified key.
        If the cache exceeds MAX_ITEMS, remove the last inserted key (LIFO).

        Args:
            key: The key under which the item should be stored.
            item: The item to store.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)

        self.last_key = key

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
