class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(0,len(s)):
            if (d.get(s[i]) is not None):
                d[s[i]] = 2
            else: d[s[i]] = 1
        for i in range(0, len(s)):
            if (d.get(s[i]) == 1):
                return i
        return -1
