class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem={i:1 for i in coins}

        def dfs(amount):
            if amount in mem:
                return mem[amount]
            if amount==0:
                return 0
            if amount<0:
                return float('inf')
            
            minn=float('inf')
            for i in coins:
                c=dfs(amount-i)
                minn=min(c,minn)
            
            mem[amount]=1+minn
            return 1 + minn

        ans = dfs(amount)
        return ans if ans != float('inf') else -1