class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        matrix=board

        rows = len(matrix)
        cols = len(matrix[0])

        # create new padded matrix
        padded = []

        # top row
        padded.append([0] * (cols + 2))

        # middle rows
        for row in matrix:
            padded.append([0] + row + [0])

        # bottom row
        padded.append([0] * (cols + 2))
        print(padded)
        
        res=False
        def backtrack(padded,word,r,c):
            if not word:
                nonlocal res
                res=True
                return
            if word[0]==padded[r][c]:
                temp=padded[r][c]
                padded[r][c]=0
                backtrack(padded,word[1:],r+1,c)
                backtrack(padded,word[1:],r,c+1)
                backtrack(padded,word[1:],r-1,c)
                backtrack(padded,word[1:],r,c-1)
                padded[r][c]=temp
            else:
                return 
        

        for i in range(len(padded)):
            for j in range(len(padded[i])):
                if padded[i][j]==word[0]:
                    backtrack(padded,word ,i ,j)
        return res


    
                