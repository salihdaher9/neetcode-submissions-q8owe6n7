# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def maxheight(root):
            if not root:
                return 0
            left=maxheight(root.left)
            right=maxheight(root.right)    
            return 1+ max(left,right)
        
        h=maxheight(root)
        res=[[] for i in range(h)]
        
        def dfs(root,index):
            if not root:
                return
            res[index].append(root.val)
            dfs(root.left,index+1)
            dfs(root.right,index+1)
        
            
        dfs(root,0)
        return res
            
            
