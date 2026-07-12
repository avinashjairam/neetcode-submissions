class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        # for each string, encode it as 'length#string' This creates a format
        # where each encoded piece is self-contained. Example: ['hello', 'world']
        # e.g. '5#hello5#world'

        for s in strs:
            # prefix each string with its length followed by '#' delimiter
            res += str(len(s)) + '#' + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 # pointer to track current position in encoded string

        # process then encoded string until we've cosumed all characters
        while i < len(s):
            j = i 

            # First phase: find the '#' delimiter to extract the length
            # move 'j' forward until we hit '#', building up the length digits
            while s[j] != '#':
                j += 1

            # extract the length from position i to j (exclusive)
            # this substring contains only digits representing the string length
            length = int(s[i:j])

            # move past the '#' delimiter to start of actual string data
            i = j + 1 

            # second phase: extract the string using the length we just found
            j = i + length

            # extract the string of exact length and add to result
            res.append(s[i:j])

            # move pointer to start of next encoded string (if any)
            i = j

        return res