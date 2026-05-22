# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        orig=root
        def dfs(root):
            if not root:
                return True
            l=dfs(root.left)
            r=dfs(root.right)

            if l and r :
                root.left=None
                root.right=None

                if root.val==target:
                    return True
            if l:
                root.left=None
            if r:
                root.right=None
            return False
            

            
        if dfs(root):
            return None
        return root