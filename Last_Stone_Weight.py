class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if (len(stones) == 0):
            return 0
        if (len(stones) == 1):
            return stones[0]

        stones.sort()

        y = stones.pop(-1)
        x = stones.pop(-1)
        if (x == y):
            return self.lastStoneWeight(stones)
        else:
            stones.append(y-x)
            return self.lastStoneWeight(stones)
