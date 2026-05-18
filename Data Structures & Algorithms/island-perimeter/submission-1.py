class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    for dr, dc in directions:
                        nr = row + dr
                        nc = col + dc

                        if nr < 0 or nr == rows or nc < 0 or nc == cols:
                            res += 1
                        elif grid[nr][nc] == 0:
                            res += 1

        return res