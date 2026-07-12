class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # iterative solution

        # start with an empty permutation list 
        perms = [[]]

        # iterate over each number in nums 
        for n in nums:
            # list to store the next set of perms 
            next_perms = []
            # iterate over each existing permutation 
            for p in perms:
                # insert the current number at every possible position in the permutation
                for i in range(len(p) + 1):
                    # make a copy to avoid modifying original list 
                    p_copy = p.copy()
                    # insert n at index i
                    p_copy.insert(i, n)
                    # store the new permutation
                    next_perms.append(p_copy)

            # update perms with a new set of permutations
            perms = next_perms 

        return perms 