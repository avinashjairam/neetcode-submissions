class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        # leftMost[i] = index of the first bar to the LEFT of i that is SHORTER than heights[i]
        # Initialized to -1 (meaning) no shorter bars exists to the left
        leftMost = [-1] * n 

        # First pass: find left boundaries (left to right)
        for i in range(n):
            # pop bars that are >= current height
            # we want to find the nearest bar that is strictly shorter 
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            # if stack not empty, top element is the nearest shorter bar on the left 
            if stack:
                leftMost[i] = stack[-1]

            # push current index for future bars to reference
            stack.append(i)

        stack = [] # reset stack for second pass 
        # rightMost[i] = index of the first bar to the RIGHT of i that is SHORTER than heights[i]
        # Initialized to n (meaning no shorter bar extends to the right)
        rightMost = [n] * n

        # second pass: find right boundaries (right to left)
        for i in range(n-1, -1, -1):
            # pop bars that are >= current height. We want to find the nearest bar that is strictly shorter
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            # if stack not empty, top element is the nearest shorter bar on the right
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i) # push current index for future bars to reference

        maxArea = 0

        # calculate area for each bar as the center height
        for i in range(n):
            # adjust the boundaries to get the actual range where bar i can extend 
            # - leftMost[i] is the index of first shorter bar, so rectangle starts at leftMost[i] + 1
            # - rightMost[i] is the index of first shorter bar, so rectangle ends at rightMost[i] - 1
            leftMost[i] += 1
            rightMost[i] -= 1

            # width = rightMost[i] - leftMost[i] + 1 (inclusive range)
            # area = height * width
            maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))

        return maxArea
