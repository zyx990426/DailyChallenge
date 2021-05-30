class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        number1 = 0
        number2 = 0
        while len(stack1) > 0:
            number1 = 10 * number1 + stack1.pop()
            
        while len(stack2) > 0:
            number2 = 10 * number2 + stack2.pop()
            
        number = number1 + number2
        
        # Make a new LinkedList
        dummy = ListNode(0)
        curr = dummy
        
        if number == 0:
            return dummy
        
        while number > 0:
            val = number % 10
            curr.next = ListNode(val)
            curr = curr.next
            number = number // 10
        
        return dummy.nextv