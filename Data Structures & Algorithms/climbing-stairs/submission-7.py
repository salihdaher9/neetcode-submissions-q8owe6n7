class Solution:
    def climbStairs(self, n: int) -> int:
        
        left=1
        right=1

        for i in range(n-1):
            temp=left+right
            left=right
            right=temp
        return right