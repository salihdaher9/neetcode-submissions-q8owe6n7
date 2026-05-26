import math

class Solution:
    def numSquares(self, n: int) -> int:
        mem = {}

        def dfs(n):
            if n == 0:
                return 0

            if n in mem:
                return mem[n]

            res = float('inf')
            rangee = math.floor(n ** 0.5) + 1

            # try bigger squares first
            for i in range(rangee - 1, 0, -1):
                res = min(res, 1 + dfs(n - i * i))

            mem[n] = res
            return res

        return dfs(n)