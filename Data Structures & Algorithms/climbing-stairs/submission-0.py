class Solution:
    def climbStairs(self, n: int) -> int:
        res=[0 for i in range(n+1)]
        res[0]=1
        for i in range(len(res)):
            if i+1<len(res):
                res[i+1]+=res[i]
            if i+2 < len(res):
                res[i+2]+=res[i]
        return res[-1]


        