class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0 # track maximum area found

        while l < r:
            # calculate area: width * height
            # height is limited by shorter line, width is distance between pointers
            area = min(heights[l], heights[r]) * (r -l)
            res = max(res, area) # update maximum if current is larger

            # move pointer pointing to the shorter line 
            # moving the shorter line might find a taller one (potentially increasing area)
            # moving the taller line can only decrease area (width decreases, height can't increase)
            if heights[l] <= heights[r]:
                l += 1 # left line is shorter/equal move it right
            else:
                r -= 1 # right line is shorter, move it left
        return res