# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle of the list 
        # reverse the second half 
        # merge the halves 
        if not head or not head.next: # edge case: empty list or single node
            return 

        # step #1: find the middle of the linked list using fast and slow pointers
        # when the loop ends, slow will point to the middle (or middle left)
        slow = head
        fast = head.next 

        while fast and fast.next:
            slow = slow.next # slow moves one step forward at a time
            fast = fast.next.next # fast moves two steps forward at a time 

        # at this point, slow is at the middle (for odd length) or just before middle (for even length)
        # step #2 - reverse second half of the linked list 
        second = slow.next # start of second half
        slow.next = None # break the list into two halves 

        # stand linked list reversal
        prev = None 
        
        while second:
            tmp = second.next # save the next node
            second.next = prev # reverse the current pointer
            prev = second # move prev to current
            second = tmp # move to the next node

        # After this loop, 'prev' points to the head of reversed second half
        # Step 3: merge the two halves by interleaving nodes 
        first, second = head, prev

        while second: # continue until we've used all nodes from the second half
            tmp1, tmp2 = first.next, second.next # save nodes from both lists
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2 # advance both pointers 


        