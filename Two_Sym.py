class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            if (d.get(target-nums[i]) is not None):
                return [d.get(target-nums[i]), i]
            d[nums[i]] = i

        
