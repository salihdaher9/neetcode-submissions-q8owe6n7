class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        o={}
        b={}

        for i in range(len(s)):
            o[s[i]]=o.get(s[i],0)+1
            b[t[i]]=b.get(t[i],0)+1
        return o==b
            