# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(a,height):
            if not a:
                return height
            left = dfs(a.left,height+1)
            right = dfs(a.right,height+1)

            return max(left,right)

        return dfs(root,0)
        