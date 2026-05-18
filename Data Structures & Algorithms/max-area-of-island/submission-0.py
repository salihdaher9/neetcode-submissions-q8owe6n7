class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visited=set()

        res=0
        
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(i,j):

            if i<0 or i==rows or j==cols or j<0:
                return 0
            if grid[i][j]==0:
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            mysum=1
            for r,c in directions:
                x=i+r
                y=c+j
                mysum+=dfs(x,y)
            return mysum



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited:
                    continue
                elif grid[i][j]==1:
                        res=max(dfs(i,j),res)

        return res