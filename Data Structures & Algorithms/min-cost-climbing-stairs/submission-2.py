class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res=[0 for i in range(len(cost ) +1)]
        res[0]=cost[0]
        res[1]=cost[1]
        cost.append(0)
        for i in range(2,len(res)):
            res[i]=min(res[i-1],res[i-2]) + cost[i]
        print(res)
        return res[-1]
