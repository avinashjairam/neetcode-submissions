class Solution:
    def climbStairs(self, n: int) -> int:
        # uses a space optimized bottom up dynamic programming approach
        # instead of keeping an array for all subproblems, it only stores the last two computed results
        # O(1) space
        # initialize two variables representing
        # 'one' -> the number of ways to reach the current step
        # 'two' -> the number of ways to reach the step before the current one 

        # Both start as 1 because
        # - there is 1 way to climb 1 step ([1])
        # - and also 1 way to climb 0 steps (do nothing)
        one, two = 1, 1

        # loop through steps from 1 to n-1
        # each iteration calculates the number of ways to reach the next step 
        for i in range(n-1):
            # temporarily store the current 'one' value (for shifting later)
            temp = one
            # the recurrence relation
            # ways to reach current step = ways to reach previous two steps
            one = one + two 
            # move the previous 'one' value to 'two' (shift window forward)
            two = temp 

        # after finishing the loop, 'one' holds the total ways to reach step 'n'
        return one         