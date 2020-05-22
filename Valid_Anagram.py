class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i in range(0,len(s)):
            if (d1.get(s[i]) is None):
                d1[s[i]] = 1
            else:
                temp = d1.get(s[i])
                d1[s[i]] = temp+1
        for j in range(0,len(t)):
            if (d2.get(t[j]) is None):
                d2[t[j]] = 1
            else:
                temp = d2.get(t[j])
                d2[t[j]] = temp+1

        return (d1 == d2)
        
