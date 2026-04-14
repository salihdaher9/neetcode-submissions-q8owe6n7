class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0
        for i in range(len(nums)):
            if nums[i]!=val and i==l:
                l+=1
            if nums[i]!=val and i > l:
                nums[l]=nums[i]
                nums[i]=val
                l+=1
        print(l)
        print(nums)
        return l
            
        