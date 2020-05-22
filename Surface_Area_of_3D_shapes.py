class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sa = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == len(grid)-1:
                    sa += grid[i][j]
                else:
                    sa += max(grid[i][j] - grid[i+1][j],0)

                if i == 0:
                    sa += grid[i][j]
                else:
                    sa += max(grid[i][j] - grid[i-1][j],0)

                if j == len(grid[i])-1:
                    sa += grid[i][j]
                else:
                    sa += max(grid[i][j] - grid[i][j+1],0)

                if j == 0:
                    sa += grid[i][j]
                else:
                    sa += max(grid[i][j] - grid[i][j-1],0)

                if grid[i][j] > 0:
                    sa += 2
                #print sa
        return sa
