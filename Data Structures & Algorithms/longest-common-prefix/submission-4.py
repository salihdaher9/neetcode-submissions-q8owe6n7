class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = strs[0]

        for s in strs[1:]:
            prefix = ""
            for j in range(len(s)):
                if j >= len(res):
                    break
                if s[j] == res[j]:
                    prefix += s[j]
                else:
                    break
            res = prefix

        return res