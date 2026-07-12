class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # initialize the result list and a deque to store indicies 
        output = []
        q = deque() # will store the indicies of elements in decreasing order of values 
        l = r = 0

        # expand the window by moving the right pointer (r)
        while r < len(nums):
            # maintain a decreasing order in the deque 
            # remove elements from the back of the deque if they are smaller 
            # than the current number (nums[r]) because they can never be the maximum in the current
            # or future windows

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # add the current index to the deque 
            q.append(r)

            # remove indicies from the front if they are out of the current window.
            # The left boundary of the window is at index 'l' so if the oldest index 
            # in deque (q[0] < 1), it's outside the window 

            if l > q[0]:
                q.popleft()
            
            # Once, we've processed at least k elements, i.e. window size reached. The window now
            # spans [l, r]. Append the element at the front of the deque as the current window's max
            if (r + 1) >= k:
                output.append(nums[q[0]]) # q[0] always store the index of the maximum element
                l += 1 # slide the number forward by incrementing the left pointer 

            # move the right pinter to expand the window 
            r += 1

        # return the list of maximum values for each window 
        return output 
        