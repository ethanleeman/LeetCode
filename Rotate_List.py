# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):


    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        size = 0
        current = head
        while (current != None):
            size += 1
            current = current.next

        if (size == 0):
            return head

        actualRotate = k % size
        #print(actualRotate)
        if (actualRotate == 0):
            return head


        counter = 0
        current = head
        while (counter < size - actualRotate - 1):
            current = current.next
            counter = counter + 1

        nxt = current.next
        answer = nxt
        current.next = None
        while (nxt.next != None):
            nxt = nxt.next
        nxt.next = head
        return answer
