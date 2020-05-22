# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode((l1.val + l2.val) %10 )
        current = ans
        run1 = l1.next
        run2 = l2.next
        carry = (l1.val + l2.val) / 10
        while (run1 is not None and run2 is not None):
            add = ListNode((run1.val + run2.val + carry) % 10 )
            carry = (run1.val + run2.val + carry)/10
            run1 = run1.next
            run2 = run2.next
            current.next = add
            current = current.next

        if (run1 is None) :
            temp = run1
            run1 = run2
            run2 = temp

        while (run1 is not None) :
            add = ListNode((run1.val + carry) % 10 )
            carry = (run1.val + carry)/10
            run1 = run1.next
            current.next = add
            current = current.next

        if (carry is not 0) :
            last = ListNode(carry )
            current.next = last
            current = current.next





        return ans
