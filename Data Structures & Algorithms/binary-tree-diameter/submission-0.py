# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
         # Global variable to store the diameter of a node
        
        def dfs(root):
            if not root:
                return 0 

            # Get height of left subtree
            left_height = dfs(root.left)
            right_height= dfs(root.right)


            self.diameter = max(self.diameter, left_height + right_height)


            return max(left_height, right_height) + 1 

        dfs(root)

        return self.diameter

        

        