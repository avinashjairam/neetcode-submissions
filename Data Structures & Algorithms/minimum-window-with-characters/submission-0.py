class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t is empty, there's no window to find
        if t == '':
            return ''

        # Build a frequency count for all characters in t
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 'have' counts how many unique characters from t are satisfied in the current window
        # 'need' is the total number of unique characters required from t
        have, need = 0, len(countT)

        # initialize result variables 
        # res = [left_index, right_index] of smallest valid window 
        # reslen = current smallest window length (initialized to infinity)

        res, resLen = [-1, -1], float('infinity')

        # left pointer of the sliding window 
        l = 0 

        # expand the window by moving the right pointer 'r'
        for r in range(len(s)):
            c = s[r]

            # add the current character to the window count 
            window[c] = 1 + window.get(c,0)

            # if the current character count matches the target count, one requirement is satisfied
            if c in countT and window[c] == countT[c]:
                have += 1

            # when all required characters are satisifed (have == need) try to shrink the window
            # from the left to find the smallest possible valid window
            while have == need:
                # update result if current window is smaller than the previously recorded one
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # remove the leftmost character from the window (shrink)
                window[s[l]] -=1

                # if a required character count falls below what is needed, window is no longer valid
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # move left pointer forward to continue shrinking
                l += 1
        # extract final result substring using stored indices 
        l, r = res

        # if resLen is infinity, no valid window was found 
        return s[l: r + 1] if resLen != float('infinity') else ''


