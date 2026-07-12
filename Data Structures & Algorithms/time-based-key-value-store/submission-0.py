class TimeMap:

    def __init__(self):
        self.keyStore = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # create empty list for new keys
        if key not in self.keyStore:
            self.keyStore[key] = []

        # append new [value, timestamp] pair to the list
        # assumes timestamps are added in non-decreasing order
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # initialize result and set the list of [value, timestamp] pairs for this key
        res , values = '', self.keyStore.get(key, [])

        # binary search to find the most recent timestamp <= query timestamp 
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r ) // 2 # calculate middle values 

            # if middle timestamp <= query timestamp, it's a valid candidate 
            if values[m][1] <= timestamp:
                res = values[m][0] # store the value as current best result
                l = m + 1 # search right half for potentially more recent timestamps 
            else:
                # middle timestamp is > query timestamp, search left half 
                r = m - 1

        return res
