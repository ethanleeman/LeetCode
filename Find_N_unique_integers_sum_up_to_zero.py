class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if (n == 0):
            return []
        answer = []
        for i in range(1,n):
            answer.append(i)
        answer.append(-sum(answer))
        return answer

        
