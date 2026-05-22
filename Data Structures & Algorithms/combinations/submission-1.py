class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(curr,level):
            if k<level:
                res.append(curr[1:])
                return
            for i in range(curr[-1]+1,n+1):
                curr.append(i)
                dfs(curr,level+1)
                curr.pop()


        dfs([0],1)
        return res
            
