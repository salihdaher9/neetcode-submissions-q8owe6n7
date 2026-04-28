# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return (dfs(p.left, q.left) and
                    dfs(p.right, q.right))
        
        res=False
        def bfs(root,subroot):
            if not root:
                return
            if dfs(root,subroot)==True:
                nonlocal res
                res=True
                return
            bfs(root.left,subroot)
            bfs(root.right,subroot)


        bfs(root,subRoot)
        return res