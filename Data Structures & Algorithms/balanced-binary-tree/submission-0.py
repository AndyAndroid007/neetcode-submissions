# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = 0
        def recurse(r):
            nonlocal flag
            if not r:
                return 0
            left = recurse(r.left)
            right = recurse(r.right)
            if abs(left-right) > 1:
                flag = 1
            return 1 + max(left,right)
        recurse(root)
        return True if flag == 0 else False
        
        