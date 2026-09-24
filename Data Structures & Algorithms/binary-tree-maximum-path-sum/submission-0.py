# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root):
        max_path = float("-inf")

        def dfs(node):
            nonlocal max_path

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            current = node.val + left + right
            max_path = max(max_path, current)

            return node.val + max(left, right)

        dfs(root)
        return max_path
        