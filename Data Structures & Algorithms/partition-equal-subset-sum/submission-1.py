class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        def backtrack(nums, curr_sum):
            if curr_sum == target:
                return True

            if curr_sum > target:
                return False

            if not nums:
                return False

            # take nums[0]
            if backtrack(nums[1:], curr_sum + nums[0]):
                return True

            # skip nums[0]
            if backtrack(nums[1:], curr_sum):
                return True

            return False

        return backtrack(nums, 0)