# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        prev, curr = None, slow.next 
        slow.next = None 

        # reverse the latter half 
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr 
            curr = nxt 
        
        # now merge
        first, second = head, prev 
        while second:

            temp1, temp2 = first.next, second.next 
            nxt = first.next
            first.next = second
            second.next = nxt 

            first, second = temp1, temp2 

        
