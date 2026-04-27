# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxx=0
        def dfs(root):
            if not root:
                return 0

            mid=dfs(root.left)+dfs(root.right)
            top=1 + max(dfs(root.left),dfs(root.right))
            big=max(mid,top-1)
            nonlocal maxx
            maxx=max(maxx,big)
            return top

        
        dfs(root)
        return maxx