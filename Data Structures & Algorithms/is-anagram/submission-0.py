from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        countS, countT = defaultdict(int), defaultdict(int)

        for i, j in zip(s, t):
            countS[i] += 1
            countT[j] += 1 

        return countS == countT