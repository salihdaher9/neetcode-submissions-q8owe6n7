class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        x="-"+s+"/"
        print(x)
        for i in range(1,len(x)-1):
            res+=1
            curr=1
            while x[i+curr]==x[i-curr]  :
                
                res+=1
                curr+=1
            r=i+1
            l=i
            while x[r]==x[l]:
                res+=1
                l-=1
                r+=1
        
        return res
            
             