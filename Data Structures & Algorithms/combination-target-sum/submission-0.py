class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(nums, currSum):
            if sum(currSum) == target:
                res.append(currSum[:])
                return
            if sum(currSum) > target:
                return
            if not nums:
                return
            for i in range(len(nums)):
                currSum.append(nums[i])
                backtrack(nums[i:],currSum)
                currSum.pop()


        backtrack(nums, [])
        return res