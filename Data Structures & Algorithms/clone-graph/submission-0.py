"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary to map original nodes to their cloned copies
        oldToNew = {}

        # recursive DFS function to clone each node
        def dfs(node):
            # if the node is already cloned, return the clone
            if node in oldToNew:
                return oldToNew[node]

            # create a new node with the same value 
            copy = Node(node.val)

            # store the copy in the mapping dictionary
            oldToNew[node] = copy

            # recursively clone and append all neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            # return the cloned node
            return copy 

        # if the input node is None, return None (empty graph)
        return dfs(node) if node else None 
        