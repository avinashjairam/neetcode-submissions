class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # frequency map of characters in current sliding window 
        res = 0 # max valid window size found so far 
        l = 0 # left pointer of sliding window 
        maxf = 0 # max frequency of any character in current window 

        # right pointer expands the window
        for r in range(len(s)):
            # add the character at right pointer to our window
            count[s[r]] = 1 + count.get(s[r], 0)

            # update maximum frequency - this could be a new character or an existing one
            maxf = max(maxf, count[s[r]])

            # key insight: in a window size (r - l + 1), if the most frequent 
            # character appears maxf times, we need (r- l + 1) - maxf replacements to
            # make all characters identical
            # check if current window is invalid (needs too many replacements)

            while (r -l + 1) - maxf > k:
                # window is invalid - shrink it from the left
                count[s[l]] -= 1 # remove leftmost character from count 
                l += 1 # move left pointer right 

            # current window [l, r] is valid, update result if its the largest so far 
            res = max(res, r-l + 1)

        return res