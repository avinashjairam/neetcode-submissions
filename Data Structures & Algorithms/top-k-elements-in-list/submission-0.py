class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # count frequency of each number 

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # create bucket where index = frequency, value = list of numbers
        # max possible frequency is len(nums), (all elements are the same)
        # we need indices from 0 to len(nums), hence (nums) + 1 bucket

        freq = [[] for i in range((len(nums) + 1))]

        # place each number in a bucket corresponding to its frequency
        for num, cnt in count.items():
            # numbers with frequency 'cnt' go into bucket at index 'cnt'
            # e.g. if number 5 appears 3 times, put 5 in freq[3]
            freq[cnt].append(num)

        # traverse buckets from highest frequency to lowest 
        res = []

        for i in range(len(freq) -1, 0, -1 ): # start from highest index, go down 1
            # process all numbers in the current frequency bucket
            for num in freq[i]:
                res.append(num)

                # stop as soon as we have k elements
                if len(res) == k:
                    return res