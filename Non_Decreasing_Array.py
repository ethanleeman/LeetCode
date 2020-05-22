def isSorted(nums):
    for i in range(len(nums)-1):
        if (nums[i] > nums[i+1]):
            return False
    return True

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) < 3):
            return True

        for i in range(len(nums)-1):
            if (nums[i] > nums[i+1]):
                cp1 = nums[:]
                cp2 = nums[:]
                cp1.pop(i)
                cp2.pop(i+1)
                if (isSorted(cp1)):
                    return True
                if (isSorted(cp2)):
                    return True
                return False
        return True

            
