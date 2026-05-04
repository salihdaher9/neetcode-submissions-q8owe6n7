# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res=0
        def dfs(root,maxnum):
            if not root:
                return
            if root.val >= maxnum:
                nonlocal res
                res+=1 
            maxnum=max(maxnum,root.val)
            dfs(root.left,maxnum)
            dfs(root.right,maxnum)

        dfs(root,float('-inf'))
        return res
