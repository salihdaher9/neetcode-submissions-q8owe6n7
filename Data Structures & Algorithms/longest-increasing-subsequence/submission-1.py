class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            best = 1  
            for i in range(start + 1, len(nums)):
                if nums[i] > nums[start]:
                    best = max(best, 1 + dfs(i))
 
            memo[start] = best
            return best

        res = 0

        for i in range(len(nums)):
            res = max(res, dfs(i))

        return res