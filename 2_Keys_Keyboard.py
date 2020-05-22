import math

n = 1001
dp = [None] * n
dp[1] = 0
for i in range(2,n):
    mn = i
    for j in range(2,int(math.sqrt(i))+1):
        #print i
        if (i % j == 0):
            candidates = [j,i/j]
            for c in candidates:
                #print range(n)
                #print dp
                if (dp[c] + i/c < mn):
                    mn = dp[c] + i/c
    dp[i]=mn

class Solution(object):
    def minSteps(self, n):
        return dp[n]
        
