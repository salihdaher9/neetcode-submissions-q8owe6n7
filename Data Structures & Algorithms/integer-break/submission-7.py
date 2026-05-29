class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[1] = 1

        for i in range(2, n + 1):
            maxx = 0

            for j in range(1, i):
                maxx = max(
                    maxx,
                    j * (i - j),        # don't break the rest
                    j * dp[i - j]       # break the rest
                )

            dp[i] = maxx

        return dp[n]