class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l=0
        for i in range(len(nums)):
            if i==len(nums)-1:
                nums[l]=nums[i]
                continue
            elif nums[i]!=nums[i+1]:
                temp=nums[l]
                nums[l]=nums[i]
                nums[i]=temp
                l+=1
            
        return l +1