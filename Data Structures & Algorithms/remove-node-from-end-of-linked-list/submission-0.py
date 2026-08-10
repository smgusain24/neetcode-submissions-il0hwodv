# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0 
        dummy = head 
        while dummy:
            cnt+=1 
            dummy = dummy.next 
        idx = cnt-n
        if idx == 0:
            return head.next

        dummy = head
        for i in range(cnt-1):
            if (i+1) == idx:
                dummy.next = dummy.next.next 
                break 
            dummy = dummy.next
        return head

