"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def dfs(grid):
            s = set()
            for row in grid:
                for val in row:
                    s.add(val)

            if len(s) == 1:
                return Node(grid[0][0], True, None, None, None, None)
            else:
                n = len(grid)
                mid = n // 2

                mydict = {
                    (0, 0): [[] for _ in range(mid)],
                    (0, 1): [[] for _ in range(mid)],
                    (1, 0): [[] for _ in range(mid)],
                    (1, 1): [[] for _ in range(mid)]
                }

                for i in range(n):
                    for j in range(n):
                        x = i // mid
                        y = j // mid

                        local_row = i % mid
                        mydict[(x, y)][local_row].append(grid[i][j])

                topLeft = mydict[(0, 0)]
                topRight = mydict[(0, 1)]
                bottomLeft = mydict[(1, 0)]
                bottomRight = mydict[(1, 1)]

                topLeftNode = dfs(topLeft)
                topRightNode = dfs(topRight)
                bottomLeftNode = dfs(bottomLeft)
                bottomRightNode = dfs(bottomRight)

                return Node(grid[0][0], False, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode)

        return dfs(grid)