class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:




        l=[0 for i in nums]
        l[0]=nums[0]%k
        

        for i in range(1,len(nums)):
            l[i]=((nums[i])+l[i-1])%k
        
        s={}
        for i in range(len(l)):
            if l[i] == 0 and i >= 1:
                return True
            if l[i] in s:
                if i-s[l[i]]>1:
                    return True
            else:
                s[l[i]]=i
        return False