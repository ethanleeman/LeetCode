class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        maximum = 0
        map = {}
        last = -1
        for i in range(l) :
            if (map.get(s[i]) is not None) :
                last = max(map.get(s[i]),last)
            map[s[i]] = i
            if (i - last > maximum): maximum = i - last
        return maximum
