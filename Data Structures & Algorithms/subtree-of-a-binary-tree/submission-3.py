class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(root, subroot):
            if not root and not subroot:
                return True
            if root and subroot:
                if root.val == subroot.val:
                    return dfs(root.left, subroot.left) and dfs(root.right, subroot.right)
            return False

        def dfs2(root, subroot):
            if dfs(root, subroot):
                return True

            if not root:
                return False

            return dfs2(root.left, subroot) or dfs2(root.right, subroot)

        return dfs2(root, subRoot)