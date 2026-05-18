class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visited=set()

        res=0
        
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(i,j):

            if i<0 or i==rows or j==cols or j<0:
                return 
            if grid[i][j]=="0":
                return
            if (i,j) in visited:
                return 
            visited.add((i,j))

            for r,c in directions:
                x=i+r
                y=c+j
                dfs(x,y)

                





        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited:
                    continue
                elif grid[i][j]=="1":
                        print("enter")
                        dfs(i,j)
                        res+=1

        return res