class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem={}
        wordSet = set(wordDict)

        def dfs(s):
            if not s:
                return True
            if s in mem:
                return mem[s]
            res=False
            print(s)
            for i in range(1,len(s)+1):
                if s[0:i] in wordSet:
                    print(s[0:i]+" is here")
                    res= res or dfs(s[i:])
            mem[s]=res
            return res

        return dfs(s)



 
