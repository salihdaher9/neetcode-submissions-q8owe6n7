from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur = root
        parent = None

        while cur and cur.val != key:
            parent = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if not cur:
            return root  # not found

        bigTree = cur.right
        smallTree = cur.left

        if bigTree:
            node = bigTree
            while node.left:
                node = node.left
            node.left = smallTree
            newSub = bigTree
        else:
            newSub = smallTree

        if not parent:
            return newSub
        if parent.left == cur:
            parent.left = newSub
        else:
            parent.right = newSub

        return root