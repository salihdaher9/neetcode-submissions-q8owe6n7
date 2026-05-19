from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        minutes = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    x = row + dr
                    y = col + dc

                    if x < 0 or x >= rows or y < 0 or y >= cols:
                        continue

                    if grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x, y))

            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1