class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l=0
        myset=set()
        myset.add(s[0])
        res=1
        for r in range(1,len(s)):
            print(myset)
            print(res)
            if s[r] in myset :
                print(s[r])

                while s[r] in myset : 
                    myset.remove(s[l])
                    l+=1
                myset.add(s[r])
            else:
                print(s[r])
                print("here")
                myset.add(s[r])
                print(myset)
            res=max(res,len(myset))
        return res

            
        