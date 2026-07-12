class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # initialize result array with 1s

        # First pass: store prefix products in result array
        # res[i] will contain product of all elements before index i
        prefix = 1 # running product of elements seen so far 

        for i in range(len(nums)):
            res[i] = prefix # store product of everything before current element
            prefix *= nums[i] # update prefix to include current element for next iteration

        # second pass: multiply by suffix products
        # res[i] already has prefix, now multiply by product of all elements after
        postfix = 1 # running product of elements seen so far (from right)

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix # multiply existing prefix product by suffix product
            postfix *= nums[i] # update postfix to include current element for next iteration

        return res
        