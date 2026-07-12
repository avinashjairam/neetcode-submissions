class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # map to store the length of consecutive sequence that includes each number
        # mp[num] = length of consecutive sequence containing num 
        mp = defaultdict(int)
        res = 0

        for num in nums:
            # only process if we haven't seen this number before 
            # mp[num] == 0 means unprocessed (defaultdict returns 0 for missing keys)
            if not mp[num]:
                # formula: new sequence length = left_length + right_length + 1 (current)
                # mp[num -1] = length of sequence ending at (num - 1)
                # mp[num +1] = length of sequence starting at (num + 1)
                # +1 for the current number itself 
                mp[num] = mp[num - 1] + mp[num + 1] + 1 
                # update the endpoints of the newly merged sequence 
                # left endpoint: num -mp[num-1] is the start of the left sequence
                # right endpoint: num + mp[num+1] is the end of the right sequence
                mp[num - mp[num - 1]] = mp[num] # update left boundary
                mp[num + mp[num + 1]] = mp[num] # update right boundary

                # track the maximum sequence length seen so far 
                res = max(res, mp[num])

        return res 

        