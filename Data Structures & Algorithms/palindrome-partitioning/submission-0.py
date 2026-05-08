class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]

        def backtrack(s,curr):
                if not s:
                    res.append(curr[:])
                    return

                for i in range(len(s)):
                    if s[:i+1] and  (s[:i+1]==s[:i+1][::-1]) :
                        print(s[:i+1])
                        curr.append(s[:i+1])
                        backtrack(s[i+1:],curr)
                        curr.pop()
        
        
        backtrack(s,[])
        return res
            