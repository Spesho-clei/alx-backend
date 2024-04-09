#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and is a caching system using LRU algorithm
    """

    def __init__(self):
        """ Initialize the LRU cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            # If key exists, remove it to update its position
            del self.cache_data[key]
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # If cache is full, remove the least recently used item (first item)
            discard_key = next(iter(self.cache_data))
            print("DISCARD:", discard_key)
            del self.cache_data[discard_key]
        
        # Add/update the key with the new value
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end to mark it as most recently used
        value = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = value
        return value
