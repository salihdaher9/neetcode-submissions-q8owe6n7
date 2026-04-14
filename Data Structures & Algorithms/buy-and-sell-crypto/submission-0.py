class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        dif=0

        for r in range(len(prices)):
            dif=max(dif,prices[r]-prices[l])
            if prices[r]<prices[l]:
                l=r
        
        return dif