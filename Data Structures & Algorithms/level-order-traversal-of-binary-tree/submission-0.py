# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        final = []
        while q:
            size = len(q)
            arr = []
            for i in range(size):
                node = q.popleft()
                if node:
                    arr.append(node.val)
                if node and node.left:
                    q.append(node.left)
                
                if node and node.right:
                    q.append(node.right)
            final.append(arr)
        return final
            
            
        