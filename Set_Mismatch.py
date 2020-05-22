class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        missing = -1
        double = -1

        for n in nums:
            if n in s:
                double = n
            else:
                s.add(n)

        for i in range(1,len(nums)+1):
            if i not in s:
                missing = i
        return [double, missing]
        
