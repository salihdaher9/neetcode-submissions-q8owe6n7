class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        def dfs(row,col):
            nonlocal visited
            if (row<0) or row>=rows:
                return 0
            if (col<0) or col>=cols:
                return 0
            if grid[row][col]==0:
                return 0
            if (row,col) in visited:
                return 0

            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            res=1
            visited.add((row,col))
            for r,c in directions:
                newrow=row+r
                newcol=col+c
                res+=dfs(newrow,newcol)
            return res
                


        res=0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    area=dfs(row,col)
                    res=max(res,area)



        return res 