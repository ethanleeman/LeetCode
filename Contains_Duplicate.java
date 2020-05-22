class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(0,len(nums)):
            if (d.get(nums[i]) is not None): return True;
            d[nums[i]] = nums[i]
        return False;
        
