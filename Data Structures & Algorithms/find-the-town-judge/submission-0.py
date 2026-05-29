class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        t={}
        trustme={}


        for i,j in trust:
            t[i]=t.get(i,0)+1
            trustme[j]=trustme.get(j,0)+1
        res=-1
        for j in trustme:
            if trustme[j]==n-1 and not j in t:
                res=j
        return res