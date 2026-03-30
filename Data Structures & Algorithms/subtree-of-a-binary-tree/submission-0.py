# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def recurse(a,b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return recurse(a.left,b.left) and recurse(a.right,b.right)
            return False
        
        if not root:
            return False
        if not subRoot:
            return True
        if recurse(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
            

        