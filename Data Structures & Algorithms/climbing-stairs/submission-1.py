class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(n):
            if  n==0:
                return 1
            if n <0 :
                return 0
            res=0
            res+=dfs(n-1)+dfs(n-2)
            return res
        
        return dfs(n)
                