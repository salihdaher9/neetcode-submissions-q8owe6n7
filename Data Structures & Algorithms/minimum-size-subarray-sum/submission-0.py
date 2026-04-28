class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sums=[0 for i in nums]
        
        for i in range(len(nums)):
            if i==0:
                sums[i]=nums[i]
            
            else:
                sums[i]=nums[i]+sums[i-1]


        l=0
        minn=len(nums)+1
        for r in range(len(sums)):
            if sums[r] >= target:
                while sums[r]-sums[l] >=target:
                    l+=1
                minn=min(minn,(r-l)+1)

        if minn==len(nums)+1:
            return 0
        
        return minn
    