class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def dfs(board, row, col, curr):

            if not curr:
                return True

            if col < 0 or col == cols:
                return False

            if row < 0 or row == rows:
                return False

            if board[row][col] == curr[0]:

                temp = board[row][col]
                board[row][col] = "#"

                if (
                    dfs(board, row + 1, col, curr[1:]) or
                    dfs(board, row - 1, col, curr[1:]) or
                    dfs(board, row, col + 1, curr[1:]) or
                    dfs(board, row, col - 1, curr[1:])
                ):
                    board[row][col] = temp
                    return True

                board[row][col] = temp

            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(board, row, col, word):
                        return True

        return False