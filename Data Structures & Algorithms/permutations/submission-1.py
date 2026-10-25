class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        
        def dfs(s):
            if len(curr)==len(nums):
                res.append(curr[:])
                return
            

            for i in nums:
                if i in s:
                    continue
                else:
                    s.add(i)
                    curr.append(i)
                    dfs(s)
                    s.remove(i)
                    curr.pop()
        
        s=set()
        dfs(s)
        return res



            
            