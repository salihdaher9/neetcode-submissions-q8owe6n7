class Solution:
    def isValid(self, s: str) -> bool:
        
        st=[]
        hashh={"[":"]","{":"}","(":")"}
        for i in s:
            if i in hashh:
                st.append(i)
            else:
                if st:
                    x=st.pop()
                    if x:
                        if i!=hashh.get(x):
                            return False
                else:
                    return False
            
        if st:
            return False
        return True
