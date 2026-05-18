class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
       
        
        res = [1 if i in coins else float('inf') for i in range(amount + 1)]

        for i in range(len(res)):
            for j in coins:
                if i+j < len(res):
                    res[i+j]=min(res[i+j],res[i]+1)
        

        if res[-1] == float('inf'):
            return -1

        return res[-1]
