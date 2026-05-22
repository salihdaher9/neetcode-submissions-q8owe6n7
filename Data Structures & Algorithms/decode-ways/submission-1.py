class Solution:
    def numDecodings(self, s: str) -> int:
        mem={}
        ns=set()
        for i in range(1,27):
            ns.add(str(i))

        def dfs(s):
            if not s:
                return 1
            if s in mem:
                return mem[s]
            
            res=0
            for i in range(len(s)):
                if s[0:i+1] in ns:
                    res+=dfs(s[i+1:])

            mem[s]=res
            return res
        
        return dfs(s)