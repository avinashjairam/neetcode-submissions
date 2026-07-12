class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start, end):
                while start <= end:
                    if s[start] != s[end]:
                        return False
                    start += 1
                    end -= 1

                return True
                
        def dfs(index, path):
            # index: current position in the string we are trying to partition
            # path: current list of palindromic strings forming a partial solution

            if index == len(s):
                # if we've reached the end of the string, store a copy of the current path
                res.append(path[:])
                return 

            # Try every possible substring, starting at index
            for i in range(index, len(s)):
                # only proceed if s[index: i + 1] is a palindrome 
                if isPalindrome(index, i):
                    # add the palindrome substring to the path 
                    path.append(s[index: i + 1])

                    # recuse on the remaining substring
                    dfs(i + 1, path)

                    # backtrack: remove the last added substring and try the next possibility
                    path.pop()

            

        res = []
        dfs(0, [])

        return res 