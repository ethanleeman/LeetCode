class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        L_clean = [0]*(N+1)
        L_extra = [0]*(N+1)

        L_clean[0] = 1
        L_extra[0] = 0
        L_clean[1] = 1
        L_extra[1] = 1
        denom = 10**9 + 7
        for i in range(2,N+1):
            L_clean[i] = (L_clean[i-2] + L_clean[i-1] + 2*L_extra[i-2]) % denom
            L_extra[i] = (L_extra[i-1] + L_clean[i-1]) % denom
        #print(L_clean)
        #print(L_extra)
        return(L_clean[-1])
        
