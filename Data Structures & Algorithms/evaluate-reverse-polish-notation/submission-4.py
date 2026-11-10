class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        ops=set()
        for i in "+-*/":
            ops.add(i)
        if len(tokens)==1:
            return int(tokens[0])
        
        for i in tokens:
            if i in ops:
                n2=int(s.pop())
                n1=int(s.pop())
                res=0
                if i=="+":
                    res=n1+n2
                if i=="-":
                    res=n1-n2
                if i=="*":
                    print(n1,n2)
                    res=n1*n2
                if i=="/":
                    print(n1,n2)

                    res=n1/n2
                s.append(res)
            else:
                s.append(i)
        

        return int(s[-1])