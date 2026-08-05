# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#if path from root to node x contains no nodes witha value greater than the value of node x
#return number of good nodes
#if child greater than parents 
#dfs with keeping track of max value(not entire path)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def helper(root, curr_max):
            nonlocal result
            if root is None:
                return
            curr_max = max(curr_max,root.val)
            if root is not None:
                if root.val >= curr_max:
                    result+=1
            helper(root.left,curr_max)

            helper(root.right,curr_max)
        helper(root,root.val)
        return result

        