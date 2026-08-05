# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return  False
        if not subRoot :
            return True
        #ans = s

        # if root.val == subRoot.val:
        #     return (sameTree(root,subRoot))?????
        if self.sameTree(root,subRoot):
            return True
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)
        if left is True or right is True:
            return True
        return False



    def sameTree(self,root1,root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None or root1 is not None and root2 is None:
            return False
        if root1.val != root2.val:
            return False
        
        left = self.sameTree(root1.left, root2.left)
        right = self.sameTree(root1.right, root2.right)

        if left is False or right is False:
            return False
        return True
    