# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def help(b):
            if p.val > b.val and q.val > b.val:
                return help(b.right)
            if p.val < b.val and q.val < b.val:
                return help(b.left)
            else:
                return b
        return help(root)
        