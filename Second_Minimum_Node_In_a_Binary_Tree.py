# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root.left is None):
            return -1

        mn = root.val
        leftsecondmin = self.findSecondMinimumValue(root.left)
        rightsecondmin = self.findSecondMinimumValue(root.right)
        l = [root.val]
        if (root.left.val not in l):
            l.append(root.left.val)
        if (root.right.val not in l):
            l.append(root.right.val)
        if (leftsecondmin not in l):
            if (leftsecondmin > -0.5):
                l.append(leftsecondmin)
        if (rightsecondmin not in l):
            if (rightsecondmin > -0.5):
                l.append(rightsecondmin)

        l.sort()

        if (len(l) == 1):
            return -1
        return l[1]

       
