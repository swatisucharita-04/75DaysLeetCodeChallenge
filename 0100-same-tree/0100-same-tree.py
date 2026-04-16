# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # Case 1: both are None
        if not p and not q:
            return True
        
        # Case 2: one is None OR values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Case 3: check left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)