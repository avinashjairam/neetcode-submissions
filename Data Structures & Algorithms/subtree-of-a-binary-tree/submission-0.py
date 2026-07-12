# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            if not p and not q:
                return True 

            if p and q and p.val == q.val:
                return same_tree(p.left, q.left) and same_tree(p.right, q.right)
            else:
                return False 

        def bfs(r, s):
            if not r and not s:
                return True 

            if not r or not s:
                return False 

            r_queue = deque([r])
    
            while r_queue:
                r_node = r_queue.popleft()

                if same_tree(r_node, s):
                    return True 

                if r_node.left:
                    r_queue.append(r_node.left)
                if r_node.right:
                    r_queue.append(r_node.right)   

            return False

        return bfs(root, subRoot)



