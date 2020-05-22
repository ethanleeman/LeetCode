class Solution(object):
    def binary_search(self, nums, key, left_inc, right_exc):
        if (right_exc - left_inc == 0):
            return -1
        if (right_exc - left_inc == 1):
            if (nums[left_inc] == key):
                return left_inc
            return -1
        if (right_exc - left_inc == 2):
            if (nums[left_inc] == key):
                return left_inc
            if (nums[left_inc + 1] == key):
                return left_inc + 1
            return -1
        middle = (right_exc + left_inc) // 2
        if (nums[middle] < key):
            return self.binary_search(nums,key, middle+1, right_exc)
        return self.binary_search(nums,key,left_inc, middle+1)



    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        totals = [0]*101
        for n in nums:
            totals[n] += 1
        less_thans = [0]*101
        running_total = 0
        for i in range(0,100):
            running_total += totals[i]
            less_thans[i+1] = running_total
        output = []
        for n in nums:
            output.append(less_thans[n])
        return output
