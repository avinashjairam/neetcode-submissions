class DoublyLinkedList:
    def __init__(self, val, next = None, prev = None):
        self.val = val # val of the current node (either number or operator)
        self.next = next  # pointer to the next node
        self.prev = prev # pointer to the previous node

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Build a doubly linked list from the tokens 
        head = DoublyLinkedList(tokens[0])
        curr = head 

        # Connect all tokens into a linkedlist (bi-directional)
        for i in range(1, len(tokens)):
            curr.next = DoublyLinkedList(tokens[i], prev = curr)
            curr = curr.next 

        # Traverse the list, evaluate operators as they appear 
        while head is not None:
            # when we find an operator node, compute its result 
            if head.val in '+-*/':
                # fetch the two previous operands 
                l =int(head.prev.prev.val)
                r = int(head.prev.val)

                # compute based on the operator
                if head.val == '+':
                    res = l + r
                elif head.val == '-':
                    res = l - r
                elif head.val == '*':
                    res = l * r
                else:
                    res = int(l/r) # truncate division towards zero 

                # replace operator node's value with the computed result 
                head.val = str(res)
                # remove the operand nodes (head.prev and head.prev.prev)
                # reconnect the list to skip them 
                head.prev = head.prev.prev.prev

                if head.prev is not None:
                    head.prev.next = head

            # keep track of the last evaluated result
            ans = int(head.val)
            head = head.next 

        # return the final computed result 
        return ans 
       
        
