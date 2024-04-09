#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and is a caching system using MRU algorithm
    """

    def __init__(self):
        """ Initialize the MRU cache
        """
        super().__init__()
        self.order_of_keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            # If key exists, remove it from the order_of_keys
            self.order_of_keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # If cache is full, remove the most recently used item
            discard_key = self.order_of_keys.pop()
            print("DISCARD:", discard_key)
            del self.cache_data[discard_key]
        
        # Add/update the key with the new value
        self.cache_data[key] = item
        self.order_of_keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end to mark it as most recently used
        self.order_of_keys.remove(key)
        self.order_of_keys.append(key)
        return self.cache_data[key]
