# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.helper(root)[0]
    
    
    def helper(self, root):
        if not root:
            return True, None, None
        
        left, leftmin, leftmax = self.helper(root.left)
        right, rightmin, rightmax = self.helper(root.right)
        
        if not left or not right:
            return False, None, None
        if leftmax is not None and leftmax >= root.val:
            return False, None, None
        if rightmin is not None and rightmin <= root.val:
            return False, None, None
        
        minNode = leftmin if leftmin is not None else root.val
        maxNode = rightmax if rightmax is not None else root.val
        
        return True, minNode, maxNode