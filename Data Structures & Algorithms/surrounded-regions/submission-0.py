from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        visited = set()

        def dfs(row, col, region):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if board[row][col] == "X":
                return False

            if (row, col) in visited:
                return False

            visited.add((row, col))
            region.append((row, col))

            touches_border = False

            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                touches_border = True

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if dfs(nr, nc, region):
                    touches_border = True

            return touches_border

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row, col) not in visited:
                    region = []
                    touches_border = dfs(row, col, region)

                    if not touches_border:
                        for r, c in region:
                            board[r][c] = "X"