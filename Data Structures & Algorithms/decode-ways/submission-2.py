class Solution:
    def numDecodings(self, s: str) -> int:
        ns = set()
        for i in range(10, 27):
            ns.add(str(i))

        nss = set()
        for i in range(1, 10):
            nss.add(str(i))

        mem = {}

        def dfs(s):
            if s in mem:
                return mem[s]

            if not s:
                return 1

            res = 0

            # Take one digit
            if s[-1] in nss:
                res += dfs(s[:-1])

            # Take two digits
            if len(s) >= 2 and s[-2:] in ns:
                res += dfs(s[:-2])

            mem[s] = res
            return res

        return dfs(s)