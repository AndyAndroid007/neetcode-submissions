# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0
        def recurse(r):
            nonlocal maxDiam
            if not r:
                return 0
            left = recurse(r.left)
            right = recurse(r.right)

            maxDiam = max(maxDiam, left + right)
            return 1 + max(left,right)
        recurse(root)
        return maxDiam
        