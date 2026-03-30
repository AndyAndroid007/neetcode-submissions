# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        flag = True
        def recurse(a,b):
            nonlocal flag
            if ((not a and b) or (not b and a)):
                flag = False
                return
            elif not a and not b:
                return
            elif a.val != b.val:
                flag = False
                return
            recurse(a.left,b.left)
            recurse(a.right,b.right)
        recurse(p,q)
        return flag
        