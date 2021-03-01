# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not p and not q:
            return None
        
        
        node = root
        
        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left

            elif node.val < p.val and node.val < q.val:
                node = node.right
                
            else:
                return node