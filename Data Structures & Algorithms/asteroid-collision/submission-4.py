class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        left=asteroids
        print(left)
        right=[]

        while left:
            if not right:
                right.append(left.pop())
                continue
            astl=left[-1]
            astr=right[-1]


            if (astl<0 and astr<0) or (astl>0 and astr>0) :
                right.append(astl)
                left.pop()
            elif astr>0:
                right.append(astl)
                left.pop()
            else:
                if abs(astl)>abs(astr):
                    right.pop()
                elif abs(astl)<abs(astr) :
                    left.pop()
                    continue
                else:
                    right.pop()
                    left.pop()
        
        return right[::-1]

