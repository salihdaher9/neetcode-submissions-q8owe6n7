# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        res=float('inf')
        def dfs(p,q,n):
            nonlocal res
            if not n:
                return 
            if n.val>p.val and n.val>q.val:
                dfs(p,q,n.left)
            
            if n.val<p.val and n.val<q.val:
                dfs(p,q,n.right)
            if (n.val>=p.val and n.val<=q.val) or (n.val<=p.val and n.val>=q.val):
                res=n
                return
            
        
        dfs(p,q,root)
        return res