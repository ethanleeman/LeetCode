class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = {}
        for i in range(0,len(J)):
            d[J[i]] = J[i]
        curr = 0
        for i in range(0,len(S)):
            if (d.get(S[i]) is not None): curr += 1
        return curr
        
