class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # early termination: if s1 is longer than s2, no permutation of s1
        # can exist as substring of s2

        if len(s1) > len(s2):
            return False 

        # use arrays of size 26 for character frequency counting 
        # index 0 = 'a', index 1 = 'b', .....index 25 = '2'
        s1Count, s2Count = [0] * 26, [0] * 26

        # initialize: count frequencies for s1 and first window of s2
        # window size: len(s1) since we're looking for permutations of s1
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # count chars in s1
            s2Count[ord(s2[i]) - ord('a')] += 1 # count chars in first window of s2 

        # count how many character frequencies currently match 
        # if matches == 26, all characters have identical frequencies 
        matches = 0

        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # sliding window approach: move window one position at a time 
        l = 0 # left pointer of sliding window 

        for r in range(len(s1), len(s2)): # right pointer extends window 
            # check if current window is a valid permutation 
            if matches == 26:
                return True 

            # Add new character (s2[r]) to the right side of window 
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1 

            # update matches count after adding new character
            if s1Count[index] == s2Count[index]:
                # frequencies now match increment matches 
                matches += 1 
            elif s1Count[index] + 1 == s2Count[index]:
                # frequencies no longer match (we had a match before adding)
                matches -= 1

            # remove old character s2[l] from the left side of window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1

            # update matches count after removing old character 
            if s1Count[index] == s2Count[index]:
                # frequencies now match - increment matches 
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                # frequencies no longer match (we had a match before removing)
                matches -= 1

            # move left pointer to maintain window size
            l += 1

        # final check: see if the last window position is a valid permutation 
        return matches == 26

        