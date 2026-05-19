
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647

        q = deque()
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        # Add ALL treasures first
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                if grid[nr][nc] != INF:
                    continue

                grid[nr][nc] = grid[row][col] + 1
                q.append((nr, nc))