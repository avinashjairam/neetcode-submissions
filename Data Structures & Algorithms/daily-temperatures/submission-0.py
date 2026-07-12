class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) # initialize result list with zeros 
        stack = [] # will store pairs (temperature, index)

        # loop through each day's temperature 
        for i, t in enumerate(temperatures):
            # while current temperature is higher than the last one in stack
            # it means we've found a warmer day for that earlier day 
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() # get previous cooler day 
                res[stackInd] = i - stackInd # compute days waited 
            
            # Push the current day onto the stack 
            stack.append((t, i))

        return res 

        