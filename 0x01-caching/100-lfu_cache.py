#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class implements a Least Frequently Used (LFU) caching system.
    It inherits from BaseCaching and follows the LFU algorithm to discard
    the least frequently used item when the cache exceeds its size limit.
    If there is a tie, it uses the LRU algorithm to discard the least
    recently used item.
    """

    def __init__(self):
        """Initialize the LFUCache class."""
        super().__init__()
        self.freq = {}
        self.lru = {}
        self.usage_count = 0

    def put(self, key, item):
        """
        Add an item in the cache. If the cache exceeds its limit,
        discard the least frequently used item.
        If there is a tie in frequency, discard the least recently used item.

        Args:
            key (str): The key for the cache.
            item (str): The value for the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key = min(
                    self.freq, key=lambda k: (self.freq[k], self.lru[k])
                )
                del self.cache_data[lfu_key]
                del self.freq[lfu_key]
                del self.lru[lfu_key]
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.freq[key] = 1

        self.usage_count += 1
        self.lru[key] = self.usage_count

    def get(self, key):
        """
        Get an item by key. If the key exists, update
        its frequency and order of access.

        Args:
            key (str): The key to retrieve the value.

        Returns:
        str: The value associated with the key or None
        if the key doesn't exist.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_count += 1
        self.lru[key] = self.usage_count

        return self.cache_data[key]
