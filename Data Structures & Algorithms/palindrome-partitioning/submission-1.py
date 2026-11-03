class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        if len(s)==1:
            return [[s]]
        res=[]


        def dfs(s,curr):
            if not s:
                res.append(curr[::])

            for i in range(len(s)):
                if s[:i+1]==s[:i+1][::-1]:
                    curr.append(s[:i+1])
                    dfs(s[i+1:],curr)
                    curr.pop()
            

        dfs(s,[])
        return res 

