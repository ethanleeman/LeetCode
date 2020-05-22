class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited, heap = set(), [(grid[0][0], 0, 0)]
        time, N = 0, len(grid)
        while heap:
            cur, x, y = heapq.heappop(heap)
            visited.add((x,y))
            time = max(time, cur)
            if x == y == N-1:
                return time
            for i, j in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if 0<=i<=N-1 and 0<=j<=N-1 and not (i,j) in visited:
                    heapq.heappush(heap, (grid[i][j],i,j))
        return -1
        
