class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res=[]

        def gen(n,curr,left,right):
            if len(curr)==n*2:
                res.append(curr)
                return
            
            if left==right:
                curr+=("(")
                gen(n,curr,left+1,right)
                return
            if left==n:
                curr+=(")")
                gen(n,curr,left,right+1)
                return
            
            curr+=("(")
            gen(n,curr,left+1,right)
            curr=curr[:-1]
            curr+=(")")
            gen(n,curr,left,right+1)
            return
        gen(n,"",0,0)

        return res

