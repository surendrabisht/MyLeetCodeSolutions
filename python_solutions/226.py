# Definition for a binary tree node.
from TreeNode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root = self.__processNodeAtCurrentLevel(root)
        return root

    def __processNodeAtCurrentLevel(self, root: TreeNode):
        leftNode = root.left
        root.left = root.right
        root.right = leftNode
        if root.left is not None:
            root.left = self.__processNodeAtCurrentLevel(root.left)
        if root.right is not None:
            root.right = self.__processNodeAtCurrentLevel(root.right)
        return root


if __name__ == "__main__":
    left_subtree = TreeNode(3, TreeNode(1), TreeNode(4))
    right_subtree = TreeNode(10, TreeNode(8), TreeNode(20))
    input = TreeNode(5, left_subtree, right_subtree)
    print(input)
    output = Solution().invertTree(input)
    print(output)
