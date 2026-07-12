class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # stack to keep track of opening brackets

        # map closing brackets to their opening pairs
        closeToOpen = {')': '(', ']':'[', '}':'{'}

        for c in s:
            if c in closeToOpen: # character is a closing bracket 
                # check if we have a matching opening bracket at top of stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # valid pair found, remove the opening bracket
                else:
                    # either stack is empty (no opening bracket) or 
                    # top doesn't match (wrong type of bracket)
                    return False 
            else:
                # character is an opening bracket 
                stack.append(c) # push to stack, wait for closing pair
        # valid only if all opening brackets were matched (stack is empty)
        return True if not stack else False 
        


        