# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case: if no lists provided, return None
        if not lists:
            return None 

        # divide and conquer: repeatedly merge list in pairs until only one remaining
        # this creates a binary like merging pattern 
        while len(lists) > 1:
            mergedLists = [] # store the results of this round of merging 

            # process lists in pairs (i, i+1), (i+2, i+3), etc. 
            # step by 2 to handle pairs 
            for i in range(0, len(lists), 2):
                l1 = lists[i] # first list in the pair

                # second list in the pair (handle odd number of lists)
                # if we're at the last list, and there's no pair, l2 becomes None 
                l2 = lists[i + 1] if i + 1 < len(lists) else None 

                # merge the two lists and add result to merged_lists
                mergedLists.append(self.mergeTwoLists(l1, l2))

            # replace the original lists with the merged results 
            # this reduces the number of lists by approximately half each iteration 
            lists = mergedLists 

        # after all iterations, only one merged list remains 
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        # merges two sorted linked lists into one sorted list
        # uses the standard two pointer technique for merging sorted sequences 
        dummy = ListNode(0)
        cur = dummy # current pointer for building the result list

        # compare nodes from both lists and attach the smaller one 
        # continue until one of the lists is exhausted 

        while l1 and l2:
            if l1.val <= l2.val:
                # l1's value is smaller or equal, so attach l1
                cur.next = l1
                l1 = l1.next # move l1 pointer forward
            else:
                # l2's value is smaller so attach l2
                cur.next = l2
                l2 = l2.next 

            # move the current pointer forward to the newly attached node 
            cur = cur.next 

        # at least one of l1 or l2 is now None 
        # attach the remaining nodes from whichever list isn't exhausted 
        # since both lists were sorted, all remaining nodes are already in order 
        cur.next = l1 or l2 

        # return the merged list, skipping the dummy node 
        return dummy.next 