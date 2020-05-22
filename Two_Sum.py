class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            soln = d.get(target - nums[i])
            if(soln != None):
                return [soln, i]

            d[nums[i]] = i
