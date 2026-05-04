class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        count = 0
        xx=x
        
        while n > 0:
            n //= 10
            count += 1
        res=0

        for i in range(count-1,-1,-1):
            num=x%10
            res+=num*(10**i)
            x //=10

        
        return res==xx