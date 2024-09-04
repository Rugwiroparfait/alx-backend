#!/usr/bin/env python3
"""
MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class implements a Most Recently Used (MRU) caching system.
    It inherits from BaseCaching and follows the MRU algorithm to discard
    the most recently used item when the cache exceeds its size limit.
    """

    def __init__(self):
        """Initialize the MRUCache class."""
        super().__init__()
        self.mru_order = []  # List to maintain the order of usage for MRU

    def put(self, key, item):
        """
        Add an item in the cache. If the cache exceeds its limit,
        discard the most recently used item.

        Args:
            key (str): The key for the cache.
            item (str): The value for the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """
        Get an item by key. If the key exists, update the order
        as it has been recently used.

        Args:
            key (str): The key to retrieve the value.
        Returns:
        str: The value associated with
        the key or None if the key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        self.mru_order.remove(key)
        self.mru_order.append(key)

        return self.cache_data[key]
