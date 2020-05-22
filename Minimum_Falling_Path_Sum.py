class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        cp = A[:]
        for y in range(1,len(cp)):
            for x in range(len(cp[y])):
                L = [cp[y-1][x]]
                if (x != 0):
                    L.append(cp[y-1][x-1])
                if (x != len(cp[y])-1):
                    L.append(cp[y-1][x+1])
                mn = min(L)
                val = cp[y][x]
                cp[y][x] = val + mn
        return min(cp[-1])
        
