class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        comb = []
        candidates.sort()

        def helper(i, results,  comb, candidates):
            if sum(comb) == target:
                results.append(comb.copy())
                return 

            if i >= len(candidates):
                return 

            comb.append(candidates[i])

            helper(i + 1, results, comb, candidates)
            
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 

            comb.pop()
            helper(i + 1, results, comb, candidates)

        helper(0, results, comb, candidates)

        return results 