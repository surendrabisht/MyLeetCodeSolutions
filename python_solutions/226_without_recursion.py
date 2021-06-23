# Definition for a binary tree node.
from TreeNode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = []
        if root is not None:
            queue.append(root)
            
        while len(queue) > 0:
            tree_node = queue.pop(0)
            left_node = tree_node.left
            tree_node.left = tree_node.right
            tree_node.right = left_node

            if tree_node.left is not None:
                queue.append(tree_node.left)
            if tree_node.right is not None:
                queue.append(tree_node.right)

        return root


if __name__ == "__main__":
    left_subtree = TreeNode(3, TreeNode(1), TreeNode(4))
    right_subtree = TreeNode(10, TreeNode(8), TreeNode(20))
    input = TreeNode(5, left_subtree, right_subtree)
    print(input)
    output = Solution().invertTree(input)
    print(output)
