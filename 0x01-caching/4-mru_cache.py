#!/usr/bin/env python3
""" MRUCache module that implements a caching system using the MRU algorithm.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that removes the most recently used item
    when the maximum capacity is exceeded.
    """

    def __init__(self):
        """Initialize the MRUCache instance."""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """
        Add an item to the cache and manage eviction using MRU policy.

        Args:
            key: The key under which the item is stored.
            item: The value to store.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.access_order.remove(key)
            self.access_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict most recently used item
                mru_key = self.access_order.pop()
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """
        Retrieve an item by key and mark it as most recently used.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark key as most recently used
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
