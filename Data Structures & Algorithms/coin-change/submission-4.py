class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        mem={}
        for i in coins:
            mem[i]=1
        if amount==0:
            return 0

        def dfs(amount):
            if amount in mem:
                if mem[amount]==-1:
                    return [-1,False]
                else:
                    return [mem[amount],True]

            if amount < 0:
                return [-1,False]
            
            if amount==0:
                return [0,True]
            
                
            res=[float('inf'),False]
            for i in coins:
                x=dfs(amount-i)
                if x[1]==True:
                    res[0]=min(res[0],x[0]+1) 
                    res[1]=True
                elif x[1]==False:
                    mem[amount-i]=-1
            if res[1]:
                mem[amount]=res[0] 
            return res



        res=dfs(amount)
        if res[1]==False:
            return -1
        else:
            return res[0]
        