# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(root, left_range,right_range):
            if not root:
                return True
            if root.val <= left_range or root.val >= right_range:
                return False
            return DFS(root.left,left_range,root.val) and DFS(root.right,root.val,right_range)
        return DFS(root,float("-inf"),float("inf"))

            