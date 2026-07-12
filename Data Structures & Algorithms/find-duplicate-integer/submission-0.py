class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # step 1 - initialize two pointers - slow and fast - starting at index 0 
        slow, fast = 0, 0

        # step 2 - find the intersection point inside the cycle
        # this works because the problem guarantees at least one duplicate which creates the cycle
        while True:
            # move slow pointer by one step
            slow = nums[slow]

            # move fast pointer by two steps
            fast = nums[nums[fast]]
            
            # if slow and fast meet, we are inside the cycle
            if slow == fast:
                break 

        # step 3 - find the entrance to the cycle (i.e. duplicate numbers)
        # reset one pointer to the start (index 0)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

            
        