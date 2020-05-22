class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = -1
        total = 0
        for n in nums:
            if (n == curr):
                total += 1
            else:
                if total == 0:
                    curr = n
                    total = 1
                else:
                    total -= 1
        return curr

        
