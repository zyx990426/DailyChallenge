class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = []
        
        queue = collections.deque([root])
        while queue:
            subset = []
            for _ in range(len(queue)):
                node = queue.popleft()
                subset.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            output.append(subset)
            
        return output