class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur=float('-inf')
        res=float('-inf')
        for i in nums:
            if cur>0:
                cur+=i
            else:
                cur=i
            res=max(res,cur)

        return res