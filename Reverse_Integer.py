class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x == 0):
            return 0

        while (x % 10 == 0):
            x /= 10


        if (x < 0):
            s = str(x)[1:]
            rev_s = '-' + s[::-1]
            rev = int(rev_s)
            if (str(rev) != rev_s):
                return 0
            if rev < -2**31:
                return 0
            return rev
        s = str(x)
        rev_s = s[::-1]
        rev = int(rev_s)
        if (str(rev) != rev_s):
            return 0
        if rev > 2**31-1:
            return 0
        return rev

        
