class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L, A = len(nums), []
        for i in range(0,L,2):
            A.extend(nums[i]*[nums[i+1]])
        return A
