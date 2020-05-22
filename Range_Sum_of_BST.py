# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        sm = 0
        d = collections.deque()
        d.appendleft(root)
        while (len(d) > 0):
            curr = d.pop()
            ## do thing
            if curr.val >= L:
                if curr.val <= R:
                    sm += curr.val
            if (curr.left):
                if (curr.val >= L):
                    d.appendleft(curr.left)
            if (curr.right):
                if (curr.val <= R):
                    d.appendleft(curr.right)

        return sm
