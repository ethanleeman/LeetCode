class Solution:
    def dfs(self,freq):
        sm = 0
        for i in range(len(freq)):
            if (freq[i] == 0):
                continue
            sm += 1
            freq[i] = freq[i] - 1
            sm += self.dfs(freq)
            freq[i] = freq[i] + 1
        return sm

    def numTilePossibilities(self, tiles):
        freq = [0]*26
        for t in tiles:
            freq[ord(t) - ord('A')] += 1
        return self.dfs(freq)
