# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node that points to the head
        # this helps handle edge cases like removing the head node itself
        dummy = ListNode(0, head)

        # initialize two pointers - left starts at the dummy node
        # right starts at the head of the list 
        left = dummy
        right = head 

        # step 1: move the right pointer 'n' steps ahead
        # this creates a gap of 'n' nodes between left and right 
        while n > 0:
            right = right.next
            n -= 1

        # step 2: move both pointers one step at time until the right reaches the end
        # at this point, left will be just before the node to be removed 
        while right:
            left = left.next
            right = right.next 

        # step 3: skip the target node by changing the left pointer's next
        left.next = left.next.next 

        # step 4: return the new head of the list. This handles the case where the 
        # original head was removed
        return dummy.next 