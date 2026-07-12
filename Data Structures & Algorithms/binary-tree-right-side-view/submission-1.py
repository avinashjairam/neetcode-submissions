from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Do a level order traversal, store each level in a list, then go through each item in the list, extracting the last item 

        # As I am doing a level order traversal, the last item in the queue is the right most item 
        if not root:
            return []

        queue = deque([root])

        results = []

        while queue:
            

            queue_length = len(queue)

            for x in range(queue_length):

                node = queue.popleft()
                
                if x == queue_length - 1:
                    results.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return results 



        

        