import heapq

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        s = sum(nums)

        mod1 = []
        mod2 = []
        for n in nums:
            if n % 3 == 1:
                heapq.heappush(mod1,n)
            if n % 3 == 2:
                heapq.heappush(mod2,n)

        if s % 3 == 0:
            return s

        if s % 3 == 1:
            if len(mod1) == 0 and len(mod2) < 2:
                return 0

            if len(mod1) == 0:
                return s - heapq.heappop(mod2) - heapq.heappop(mod2)

            if len(mod2) < 2:
                return s -heapq.heappop(mod1)

            min1 = heapq.heappop(mod1)
            min2 = heapq.heappop(mod2) + heapq.heappop(mod2)
            return s - min(min1,min2)


        if s % 3 == 2:
            if len(mod2) == 0 and len(mod1) < 2:
                return 0

            if len(mod2) == 0:
                return s - heapq.heappop(mod1) - heapq.heappop(mod1)

            if len(mod1) < 2:
                return s - heapq.heappop(mod2)

            min1 = heapq.heappop(mod1) + heapq.heappop(mod1)
            min2 = heapq.heappop(mod2)
            return s - min(min1,min2)

        return 0
