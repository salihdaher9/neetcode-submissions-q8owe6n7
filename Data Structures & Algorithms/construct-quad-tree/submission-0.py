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
            first=grid[0][0]
            s = set()
            for row in grid:
                for val in row:
                    s.add(val)

            if len(s) == 1:
                return Node(grid[0][0], True, None, None, None, None)
            else:
                            
                n = len(grid)
                mid = n // 2

                topLeft = [row[:mid] for row in grid[:mid]]
                topRight = [row[mid:] for row in grid[:mid]]
                bottomLeft = [row[:mid] for row in grid[mid:]]
                bottomRight = [row[mid:] for row in grid[mid:]]     

                    
                topLeftNode = dfs(topLeft)
                topRightNode = dfs(topRight)
                bottomLeftNode = dfs(bottomLeft)
                bottomRightNode = dfs(bottomRight) 
                        
                    
                return Node(first,False,topLeftNode,topRightNode,bottomLeftNode,bottomRightNode)
        return dfs(grid)
        