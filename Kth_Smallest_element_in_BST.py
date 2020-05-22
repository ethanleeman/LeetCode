# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        curr_node = root
        while len(stack) > 0 or root != None:
            while curr_node != None:
                stack.append(curr_node)
                curr_node = curr_node.left
            #print stack
            curr_node = stack.pop()
            k -= 1
            if k == 0:
                return curr_node.val
            curr_node = curr_node.right
        
