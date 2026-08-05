# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if we encouter p or q thats the answer, we have to split accordingly
        
        # cur = root
        # while cur != None:
        #     # if p == cur.value:
        #     #     return p.value
        #     # if q == cur.value:
        #     #     return q.value
        #     if (p.val < cur.val and q.val < cur.val):
        #         cur = cur.left
        #     elif (p.val > cur.val and q.val > cur.val):
        #         cur = cur.right
        #     else: 
        #         return cur

        if p is None or root is None or not q:
            return None

        if max(q.val,p.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(q.val,p.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root       


