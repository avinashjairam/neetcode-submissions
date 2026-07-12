# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, l3):
        prev = None
        cur = l3 
        nums = []

        while cur:
            tmp = cur.next
            nums.append(str(cur.val)) 
            cur.next = prev
            prev = cur 
            cur = tmp 

       
        return nums[::-1]


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = int(''.join(self.reverseList(l1)))
        y = int(''.join(self.reverseList(l2)))
        #z = str(x + y).split()
        z = [x for x in str(x+y)[::-1]]
        head = ListNode()
        cur = head
        for val in z:
            cur.next = ListNode(val)
            cur = cur.next

        return head.next



