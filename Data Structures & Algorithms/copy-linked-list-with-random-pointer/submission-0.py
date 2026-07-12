import collections
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create a default dict that automatically creates new nodes (0) for any unseen data
        # create placeholder nodes on demand 
        oldToCopy = collections.defaultdict(lambda:Node(0))

        # explicitly handle the None case - None should map to None, not a new node
        oldToCopy[None] = None # crucial for handling next/random pointers that point to None

        # start traversal from the head of the original list
        cur = head 

        # single pass through the original list 
        while cur:
            # set the val of the copied node, by this point, oldToCopy[cur] has been created
            oldToCopy[cur].val = cur.val 

            # connect the next pointer of the cop to the copy of cur.next 
            oldToCopy[cur].next = oldToCopy[cur.next]

            # connect the random pointer of the copy to the copy of cur.random
            oldToCopy[cur].random = oldToCopy[cur.random]

            # move to the next node in the original list
            cur = cur.next

        # return the copy of the original head, if head was none, this returns node
        return oldToCopy[head]
        