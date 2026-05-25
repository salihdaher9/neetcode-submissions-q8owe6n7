class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        curr = []

        def backtrack(nums, curr):
            if sum(curr) == target:
                return True

            if sum(curr) > target:
                return False

            if not nums:
                return False

            curr.append(nums[0])
            if backtrack(nums[1:], curr):
                return True

            curr.pop()
            if backtrack(nums[1:], curr):
                return True

            return False

        return backtrack(nums, curr)