#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is a caching system using LIFO algorithm
    """

    def __init__(self):
        """ Initialize the LIFO cache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the last item inserted (LIFO)
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD:", last_key)
            del self.cache_data[last_key]
            
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
