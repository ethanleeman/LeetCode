
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        if (l1.val < l2.val):
            start = l1
            l1 = l1.next
        else:
            start = l2
            l2 = l2.next
        current = start
        while (l1 != None or l2 != None):
            if (l1 == None):
                current.next = l2
                current = current.next
                l2 = l2.next
            elif (l2 == None):
                current.next = l1
                current = current.next
                l1 = l1.next
            elif (l1.val < l2.val):
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next
        return start

        
