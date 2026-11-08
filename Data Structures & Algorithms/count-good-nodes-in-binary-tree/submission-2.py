# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res=0
        minn=float('-inf')
        def dfs(root,curr):
            nonlocal res
            if not root:
                return
            
            if root.val >= curr:
                res+=1
                dfs(root.right,root.val)
                dfs(root.left,root.val)
            else:
                dfs(root.right,curr)
                dfs(root.left,curr)


        dfs(root,minn)
        return res

            