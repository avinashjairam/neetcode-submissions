from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # return if root is None
        if not root:
            return []

        # list of list to store the levels 
        levels = []

        # create a queue 
        queue = deque([root])

        # as long as the queue is not empty 
        while queue:
            current = []
          
            for _ in range(len(queue)):
                # remove the first item from the queue 
          
                node = queue.popleft() 
                current.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            levels.append(current)

        return levels 

            


