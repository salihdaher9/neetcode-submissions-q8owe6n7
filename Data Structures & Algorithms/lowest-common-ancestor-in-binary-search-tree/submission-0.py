# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res=None
        def dfs(root,p,q):
            nonlocal res
            if not root:
                return
            if root.val >= q.val and root.val <= p.val:
                res=root
                return
            if root.val >= p.val and root.val <= q.val:
                res=root 
                return
            if root.val >= p.val and root.val >= q.val:
                dfs(root.left,p,q)
            if root.val <= p.val and root.val <= q.val:
                dfs(root.right,p,q) 
        
        dfs(root,p,q)
        return res