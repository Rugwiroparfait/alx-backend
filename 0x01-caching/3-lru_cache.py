#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class implements a Least Recently Used (LRU) caching system.
    It inherits from BaseCaching and follows the LRU algorithm to discard
    the least recently used item when the cache exceeds its size limit.
    """

    def __init__(self):
        """Initialize the LRUCache class."""
        super().__init__()
        self.lru_order = []  # List to maintain the order of usage for LRU

    def put(self, key, item):
        """
        Add an item in the cache. If the cache exceeds its limit,
        discard the least recently used item.

        Args:
            key (str): The key for the cache.
            item (str): The value for the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """
        Get an item by key. If the key exists, update the order
        as it has been recently used.

        Args:
            key (str): The key to retrieve the value.

        Returns:
            str: The value associated with the key
            or None if the key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]
