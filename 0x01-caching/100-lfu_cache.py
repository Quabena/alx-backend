#!/usr/bin/env python3
""" LFUCache module that implements a caching system using
the LFU algorithm.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and implements a
    LFU (Least Frequently Used) caching system.

    If multiple keys have the same frequency, the LRU
    (Least Recently Used) one is discarded.
    """

    def __init__(self):
        """Initialize the LFUCache."""
        super().__init__()
        self.freq = {}          # Dictionary to track access frequency
        self.usage_order = []   # To track usage order for LRU tie-breaking

    def put(self, key, item):
        """
        Add an item to the cache and manage eviction using
        LFU + LRU policy.

        Args:
            key: The key under which the item is stored.
            item: The value to store.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update item and frequency
            self.cache_data[key] = item
            self.freq[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU item(s)
                min_freq = min(self.freq.values())
                candidates = [k for k in self.freq if self.freq[k] == min_freq]

                # Apply LRU among candidates
                for k in self.usage_order:
                    if k in candidates:
                        discard = k
                        break

                del self.cache_data[discard]
                del self.freq[discard]
                self.usage_order.remove(discard)
                print("DISCARD:", discard)

            # Add new key
            self.cache_data[key] = item
            self.freq[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item by key and update its frequency and usage order.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the key, or None if not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
