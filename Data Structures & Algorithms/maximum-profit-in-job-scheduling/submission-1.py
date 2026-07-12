import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    
        # Combine each job into one tuple and sort by start time
        jobs = sorted(zip(startTime, endTime, profit))

        # Extract just the start times for binary search 
        starts = [job[0] for job in jobs]

        n = len(jobs)

        # dp[i] = max profit we can earn starting from job i
        # dp[n] = 0 because there are no jobs left after the last index
        dp = [0] * (n + 1)

        # Work backwards so dp[i + 1] and dp[next_index] are already known
        for i in range(n-1, -1, -1):
            start, end, curr_profit = jobs[i]

            # Find the next job that does not overlap
            # We need first start time >= current job's end time
            next_index = bisect.bisect_left(starts, end)

            # Option 1: skip this job
            skip = dp[i + 1]

            # Option 2: take this job, then continue from next_index
            take = curr_profit + dp[next_index]

            # Best result starting at job i
            dp[i] = max(skip, take)

        return dp[0]