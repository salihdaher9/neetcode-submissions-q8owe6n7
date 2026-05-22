class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def dfs(n,k,curr,level):
            if k<level:
                res.append(curr[1:])
                return
            for i in range(curr[-1]+1,n+1):
                curr.append(i)
                dfs(n,k,curr,level+1)
                curr.pop()


        dfs(n,k,[0],1)
        return res
            
