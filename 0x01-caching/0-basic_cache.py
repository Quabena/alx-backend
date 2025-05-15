#!/usr/bin/env python3
"""
BasicCache module that implements a simple caching
system with no limit.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache is a simple caching system that stores data in memory
    without any eviction policy or item limit.
    """

    def put(self, key, item):
        """
        Add an item to the cache using the specified key.
        If key or item is None, the method does nothing.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache using the specified key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is None
            or does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
