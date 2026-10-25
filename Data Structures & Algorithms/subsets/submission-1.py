class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        res=[]
        def dfs(curr,nums):
            if not nums:
                res.append(curr[:])
                return 
            curr.append(nums[0])
            dfs(curr,nums[1:])
            curr.pop()
            dfs(curr,nums[1:])
        
        dfs([],nums)
      
        return res
            