# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    flag = 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def find_height(root):
            if not root:
                return 0 

            left_height = find_height(root.left)
            right_height =  find_height(root.right)

            if abs(left_height - right_height) > 1:
                self.flag -= 1 
               


            return max(left_height, right_height) + 1 
        
        find_height(root)

        return self.flag == 1
     
