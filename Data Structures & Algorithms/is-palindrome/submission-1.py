class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # two pointers: left start at beginning, right at end

        while l < r:
            # skip non-alphanumeric characters from the left
            # move left pointer forward until we find an alphanumeric character
            while l < r and not self.alphaNum(s[l]):
                l += 1

            # skip non-alphanumeric characters from the right
            # move right pointer backward until we find an alphanumeric character
            while r > l and not self.alphaNum(s[r]):
                r -= 1

            # compare the characters (case -insensitive). If they don't match it's not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            
            # move both pointers inward for next comparison
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        # check if character is alphanumeric using ASCII values
        # 'A'-'Z': 65-90, 'a'-'z': 91-122, '0'-'9': 48-57
        return (ord('A') <= ord(c) <= ord('Z') or 
               ord('a') <= ord(c) <= ord('z') or 
               ord('0') <= ord(c) <= ord('9'))

