class Solution:
    def climbStairs(self, n: int) -> int:

        cache={0:1}
        
        def dfs(n):
            if n in cache:
                return cache[n]
            if  n==0:
                return 1
            if n <0 :
                return 0
            res=0
            res+=dfs(n-1)+dfs(n-2)
            cache[n]=res
            return cache[n]
        
        return dfs(n)
                