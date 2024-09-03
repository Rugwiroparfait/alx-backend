#!/usr/bin/python3
""" FIFOCache module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is  a caching system that in inherits from BaseCaching.
        It used a First-In-First-Out cashing policy.
    """

    def __init__(self):
        """ Initialize the class by calling the parent class initializer.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache.
        If key or item is None, this method does nothing.
        If the cache exceeds the limit defined by MAX_ITEMS,
        the first item added to the cache is discarded.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print(f"DISCARD: {first_key}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key.
            If the key does not exist or if the key is None, return None
        """
        return self.cache_data.get(key)
