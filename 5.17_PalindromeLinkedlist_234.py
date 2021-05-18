# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
# Approach1: Use a stack, loop 2 times

        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        
        while head:
            temp = stack.pop()
            if head.val != temp.val:
                return False
            head = head.next
        
        return True