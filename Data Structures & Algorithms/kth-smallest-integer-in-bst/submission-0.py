# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        numbers = []

        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            numbers.append(root.val)
            dfs(root.right)


        dfs(root)

        return numbers[k-1]

            



