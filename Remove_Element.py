class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if (len(nums) == 0):
            return 0

        current_index = 0
        swap_index = len(nums) - 1
        while (current_index <= swap_index):
            if (nums[current_index] == val):
                nums[current_index], nums[swap_index] = nums[swap_index],nums[current_index]
                swap_index -= 1
            else:
                current_index += 1
        return swap_index + 1

        
