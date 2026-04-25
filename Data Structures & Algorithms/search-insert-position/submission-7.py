class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
                
        l=0
        r=len(nums)-1

        if target<nums[l]:
            return l
        if target>nums[r]:
            return r+1
        while l != r:
            mid=(l+r)//2
            print(mid)


            if nums[mid]>target:
                if nums[mid-1]<target:
                    return mid
                else:
                    r=mid-1
            
            elif nums[mid]<target:
                if nums[mid+1]>target:
                    return mid+1
                else:
                    l=mid+1
            elif nums[mid]==target:
                return mid
        
        if l==r:
            if nums[l]>=target:
                return r
            else:
                return r+1
        