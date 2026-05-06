class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res=[]

        def backtrack(nums,curr):
            if len(curr)==len(nums):
                res.append(curr[:])
                return
            
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    backtrack(nums,curr)
                    curr.pop()
        backtrack(nums,[])
        return res