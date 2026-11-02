class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        myset=set()

        l=0
        myset.add(s[l])
        res=1
        for r in range(1,len(s)):
            if s[r] in myset:
                while s[r] in myset:
                    myset.remove(s[l])
                    l+=1
                myset.add(s[r])
            else:
                myset.add(s[r])
                res=max(res,len(myset))
        return res