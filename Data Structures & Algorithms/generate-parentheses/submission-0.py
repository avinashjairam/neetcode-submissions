class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [] # used to build the current parentheses string 
        res = [] # list to store all valid combinations 

        # recursive helper function
        # openN = number of '(' used so far 
        # closedN = number of ')' used so far 
        def backtrack(openN, closedN):
            # Base case: when both counts reach n, meanining we have used all '(' and ')'
            if openN == closedN == n:
                res.append(''.join(stack)) # join list into string and add to results
                return 

            # case 1: we can add '(' if we haven't used up all of them as yet 
            if openN < n:
                stack.append('(') # choose '('
                backtrack(openN + 1, closedN) # explore further 
                stack.pop() # undo a choice and backtrack 

            # case 2: we can only add ')' if there are unmatched '('
            if closedN < openN:
                stack.append(')') # choose ')'
                backtrack(openN, closedN + 1) # explore further 
                stack.pop() # undo a choice adn backtrack

            # start the recursion with 0 '(' and 0 ')'
            return res 

        backtrack(0, 0)
        return res
        