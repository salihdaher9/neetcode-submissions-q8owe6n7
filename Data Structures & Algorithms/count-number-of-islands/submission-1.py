class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)-1
        cols=len(grid[0])-1

        visited=set()


        def dfs(i,j):
            if(i,j) in visited:
                return
            
            if i<0 or i>rows:
                return
            if j<0 or j>cols:
                return
            if grid[i][j]=="0":
                return
            
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        res=0
        for i in range(rows+1):
            for j in range(cols+1):
                if (i,j) not in visited and grid[i][j]=="1":
                    dfs(i,j)
                    res+=1
        return res
