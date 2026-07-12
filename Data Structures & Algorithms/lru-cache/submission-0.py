from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # use ordered dict which maintains insertion order and allows efficient reordering
        self.cache = OrderedDict()
        # store capacity (shortened variable name from capacity)
        self.cap = capacity
        

    def get(self, key: int) -> int:
        # check if keys exists in cache
        if key not in self.cache:
            # key not found - return -1 as per LRU cache convention
            return -1 

        # key found move to end to mark as most recently used
        # move_to_end() removes the key from its current position and adds it to the end
        self.cache.move_to_end(key)
        # return the value associated with the key
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # if key already exists in cache
        if key in self.cache:
            # move existing key to end (most recently used positions)
            # this must be done before updating the value to maintain correct order
            self.cache.move_to_end(key)
        # set/update the key/value pair 
        # if key exists, this updates the value, if new, this adds the entry to the end
        self.cache[key] = value 

        # check if cache exceeds capacity after adding/updating 
        if len(self.cache) > self.cap:
            # remove the least recently used item (first item in OrderedDict)
            # pop item (last = First) removes from the beginning (FIFO order)
            # pop item (last = True) would remove from the end (LIFO order)
            self.cache.popitem(last = False)
        
