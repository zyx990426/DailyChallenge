# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None
        
        cur = head
        prev = head
        
        for _ in range(n):
            cur = cur.next
        if cur is None:
            return head.next
        else:
            while cur.next:
                cur = cur.next
                prev = prev.next
            
            temp = prev.next
            prev.next = temp.next
            return head
            