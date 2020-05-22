import heapq


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        heap = [1,2]
        curr = 0
        while (curr < n):
            #print(heap)
            val = heapq.heappop(heap)
            if (val != heap[0]):
                heapq.heappush(heap,val*2)
                heapq.heappush(heap,val*3)
                heapq.heappush(heap,val*5)
                curr += 1
        return val
