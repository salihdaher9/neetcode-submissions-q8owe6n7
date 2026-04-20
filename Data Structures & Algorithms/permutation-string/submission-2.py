class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydict={}
        for i in s1:
            mydict[i]=1+mydict.get(i,0)
        

        l=0
        window={}
        for r in range(len(s2)):
            print(window)
            if (r-l)==len(s1):
                window[s2[l]]=window.get(s2[l],0)-1
                if window[s2[l]]==0:
                    del window[s2[l]]
                l+=1

            window[s2[r]]=1+window.get(s2[r],0)
            if window==mydict:
                return True
        return False


