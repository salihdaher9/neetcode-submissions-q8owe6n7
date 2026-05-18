class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res=0
        for row in range(len(grid)):
            for col in range(len(grid[row])):

                if grid[row][col]==1:
                    if row==0:
                        res+=1
                    if row == len(grid)-1:
                        res+=1
                    if row!=0:
                        if grid[row-1][col]==0:
                            res+=1
                    if row!=len(grid)-1:
                        if grid[row+1][col]==0:
                            res+=1
                
                if grid[row][col]==1:
                    if col==0:
                        res+=1
                    if col == len(grid[0])-1:
                        res+=1
                    if col!=len(grid[0])-1:
                        if grid[row][col+1]==0:
                            res+=1
                    if col!=0:
                        if grid[row][col-1]==0:
                            res+=1
        return res