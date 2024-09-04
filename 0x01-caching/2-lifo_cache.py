#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that inherits from BaseCaching.
        It uses a Last-In-First-Out (LIFO) caching policy.
    """

    def __init__(self):
        """ Initialize the class by calling the parent class initializer.
        """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the limit defined by MAX_ITEMS.
        the last item added to the cache is discarded.
        """
        if key is not None and item is not None:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data
            ):
                if self.last_key:
                    print(f"DISCARD: {self.last_key}")
                    del self.cache_data[self.last_key]

            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key.
            If the key doesn't exist or if the key is None, Return None.
        """
        return self.cache_data.get(key)
