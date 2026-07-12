from collections import deque
from pprint import pprint

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p, q):
            # If both trees are empty, they are equivalent
            if not p and not q:
                return True 

            # If one tree is empty, but the other is not, they are not equivalent
            if not p or not q:
                return False 

            # Initialize queues for BFS
            p_queue = deque([p])
            q_queue = deque([q])


            # Perform BFS
            while p_queue and q_queue:

                #Get the next nodes from both trees
                p_node = p_queue.popleft()
                q_node = q_queue.popleft()

                # If both nodes are None, they are equivalent
                if not p_node and not q_node:
                    continue

                # If one node is None and the other isn't, they are not equivalent

                if not p_node or not q_node:
                    return False 

                # If the values of the nodes are different, they are not equivalent
                if p_node.val != q_node.val:
                    return False

                # Add the left children to the queue
                p_queue.append(p_node.left)
                q_queue.append(q_node.left)
            
                # Adding the right children to the queue
                p_queue.append(p_node.right)
                q_queue.append(q_node.right)
                


            # If both queues are empty, the trees are equivalent
            return not p_queue and not q_queue

        return bfs(p,q)



            