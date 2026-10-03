# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        final = []
        q = deque([root])
        while q:
            size = len(q)
            final.append(q[-1].val)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        
        return final

        