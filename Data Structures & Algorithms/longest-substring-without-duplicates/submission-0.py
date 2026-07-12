class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # map to store the most recent index of each character
        mp = {}

        # left pointer of the sliding window 
        l = 0 

        # track maximum length found so far 
        res = 0 

        # right pointer extends the sliding window 
        for r in range(len(s)):
            # if current character was seen before in our window 
            if s[r] in mp:
                # move left pointer to position after the duplicate character 
                # use max() to ensure we don't move left pointer backwards 
                l = max(mp[s[r]] + 1, l)

            # update/store the current index of this character 
            mp[s[r]] = r

            # update the maximum length: current window size is (r - l + 1)
            res = max(res, r -l + 1)

        # return the longest substring length found
        return res

        