# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #print(nums)
        if (len(nums) == 0):
            return None
        argmax = 0
        for i in range(1,len(nums)):
            if (nums[i] > nums[argmax]):
                argmax = i

        root = TreeNode()
        root.val = nums[argmax]
        root.left = self.constructMaximumBinaryTree(nums[:argmax])
        root.right = self.constructMaximumBinaryTree(nums[argmax+1:])
        return root
