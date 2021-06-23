class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right    
    
    def __str__(self):
        queue = [self]
        values = []
        while len(queue) > 0:
            node = queue.pop(0)
            values.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        
        return str(values)