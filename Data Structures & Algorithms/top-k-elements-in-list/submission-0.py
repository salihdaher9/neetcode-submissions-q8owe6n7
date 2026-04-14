class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            c[i]=1+c.get(i,0)
        
        l=[[] for i in range(len(nums)+1)]

        for num in c:
            l[c[num]].append(num)
        x=k
        res=[]
        print(l)
        for i in range(len(nums),0,-1):
            
            while l[i]:
                if x==0:
                    return res 
                res.append(l[i].pop())
                x-=1


        return res

        

        