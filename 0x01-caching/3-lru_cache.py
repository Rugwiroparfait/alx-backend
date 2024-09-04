#!/usr/bin/env/python3
""" Least recently Used(LRU)
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        """Initialize the LRUCache class."""
        super().__init__()
        self.lru_order = []  # This will track the order of usage for LRU

    def put(self, key, item):
        """Add an item in the cache."""
        if key is None or item is None:
            return

        # If key already exists, remove it from the order list
        if key in self.cache_data:
            self.lru_order.remove(key)

        # If the cache is full, remove the least recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the item to the cache and update the order
        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """Get an item by key."""
        if key is None or key not in self.cache_data:
            return None

        # Update the order since this key was recently used
        self.lru_order.remove(key)
        self.lru_order.append(key)

        return self.cache_data[key]
