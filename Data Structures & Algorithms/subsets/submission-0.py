class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        def backtrack(nums,curr):
            if not nums:
                return
            first=nums[0]
            curr.append(first)
            print(curr)
            nonlocal res
            res.append(curr[:])
            backtrack(nums[1:],curr)
            curr.pop()
            backtrack(nums[1:],curr) 
      
        backtrack(nums,[])
        
        return res