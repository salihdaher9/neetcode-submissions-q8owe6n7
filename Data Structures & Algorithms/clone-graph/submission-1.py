"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

        oldtonew={}

        def dfs(node):
            if not node:
                return
            if node in oldtonew:
                return oldtonew[node]
            newNode=Node(node.val)
            oldtonew[node]=newNode

            for i in node.neighbors:
                neighbor=dfs(i)
                newNode.neighbors.append(neighbor)
            
            return newNode
        
        return dfs(node)