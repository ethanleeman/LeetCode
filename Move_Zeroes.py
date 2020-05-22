class Solution:
    def moveToEnd(self, nums:List[int], k:int) -> None:
        for i in range(k,len(nums)-1):
            if (nums[i+1] == 0): return
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while(i > -1):
            if (nums[i] == 0): self.moveToEnd(nums,i)
            i -= 1
