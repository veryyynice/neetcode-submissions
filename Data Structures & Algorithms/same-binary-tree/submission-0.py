# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
                
        def dfs(root_l,root_r):
            if root_l is None and root_r is not None or root_l is not None and root_r is None:
                return False
            if root_l is None and root_r is None:
                return True
            if root_l.val != root_r.val:
                return False

            left = dfs(root_l.left,root_r.left)
            right = dfs(root_l.right,root_r.right)
            if left is False or right is False:
                return False
            return True
        return dfs(p,q)
