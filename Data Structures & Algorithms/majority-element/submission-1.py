class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        count={}
        for i in nums:
            if (i in count) and (count[i]==int(len(nums)/2)):
                return i
            else:
                count[i]=count.get(i,0)+1
        