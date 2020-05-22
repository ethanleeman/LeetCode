class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        product = 1
        sm = 0
        for c in s:
            product *= (ord(c) - ord('0'))
            sm += (ord(c) - ord('0'))
        return product - sm

        
