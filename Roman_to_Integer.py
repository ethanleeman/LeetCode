class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digit = []
        for c in s:
            if (c == 'I'):
                digit.append(1)
            if (c == 'V'):
                digit.append(5)
            if (c == 'X'):
                digit.append(10)
            if (c == 'L'):
                digit.append(50)
            if (c == 'C'):
                digit.append(100)
            if (c == 'D'):
                digit.append(500)
            if (c == 'M'):
                digit.append(1000)
        index = 0
        while (index < len(digit)-1):
            if (digit[index] < digit[index+1]):
                digit[index+1] = digit[index+1] - digit[index]
                digit.pop(index)
            else:
                index += 1
        return sum(digit)
