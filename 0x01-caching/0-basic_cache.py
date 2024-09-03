#!/usr/bin/python3
""" BasicCache module
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache is a caching system that inherits from BaseCaching.
        This cache has no limit on the number of items it can store.
    """

    def put(self, key, item):
        """ Add an item in the cache.
            if key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.
            If the key doesn't exist or is None, Return None
        """
        return self.cache_data.get(key)
