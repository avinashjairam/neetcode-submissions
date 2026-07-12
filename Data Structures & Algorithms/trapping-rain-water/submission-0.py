class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) -1 # two pointers at both ends

        # track max heights seen so far from each side 
        leftMax, rightMax = height[l], height[r]
        
        res = 0

        while l < r:
            # process the side with smaller max height
            # we can safely calculate water at this side because
            # we know the max on this side (leftMax or right Max)
            # we know there's at least one bar >= this max on the other side

            if leftMax < rightMax:
                l += 1 # move left pointer inward
                # update left max if current is taller 
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1 # move right pointer inward
                # update right max if current is taller
                rightMax = max(rightMax, height[r])
                # water = max level - ground height
                res += rightMax - height[r]
        
        return res