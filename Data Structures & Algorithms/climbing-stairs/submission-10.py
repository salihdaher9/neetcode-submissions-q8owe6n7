class Solution:
    def climbStairs(self, n: int) -> int:
        seen={}
        def dfs(x):
            if x==n:
                seen[x]=1
                return 1
            if x>n:
                seen[x]=0
                return 0
            if x in seen:
                return seen[x]
            else:
                
                answer= dfs(x+1) + dfs(x+2)
                seen[x]=answer
                return answer
        return dfs(0)