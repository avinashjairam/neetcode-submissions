# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # create a dummy node to simplify edge cases
        # dummy points to the original head
        dummy = ListNode(0, head)

        # groupPrev points to the node before the current group being processed
        # initially points to dummy (before the first group)
        groupPrev = dummy

        # find k-th node from groupPrev. 
        # this will be the last node of the current group to reverse
        while True:
            kth = self.getKth(groupPrev, k)

            # if we can't find k nodes, we're done (no more complete groups)
            if not kth:
                break

            # save the first of next group (after current k-group)
            groupNext = kth.next

            # setup for reversal within current k-group, prevStarts at groupNext
            # curr starts at the first node of the current group 
            prev, curr = kth.next, groupPrev.next 

            # reverse the current k-group
            while curr != groupNext:
                tmp = curr.next # save the next node
                curr.next = prev # reverse the link 
                prev = curr # move prev forward
                curr = tmp # move cur forward 

            # after reversal connect the group with the rest of the list
            tmp = groupPrev.next # save original first node (now last after reversal)
            groupPrev.next = kth # connect previous part to new first node of group
            groupPrev = tmp # update groupPrev to the last node of reversed group 

        return dummy.next 

    def getKth(self, curr, k):
        # find the k-th node starting from curr
        # return node if there aren't k nodes available 
        while curr and k > 0:
            curr = curr.next
            k -= 1 

        return curr 
