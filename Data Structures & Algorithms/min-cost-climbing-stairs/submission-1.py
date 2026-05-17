class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        mem={}
        def dfs(n):
            if n==0 :
                return cost[0]
            if n==1:
                return cost[1]
            
            if n<0:
                return float('inf')
            if n in mem:
                return mem[n]
            
            l=dfs(n-1)
            r=dfs(n-2)

            m=min(l,r)
            mem[n]=m+cost[n]
            return m+cost[n]

        x=dfs(n-1)
        y=dfs(n-2)
        return min(y,x)