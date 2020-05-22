

def position(c):
    num = ord(c) - ord('a')
    return (num // 5, num % 5)

def seq_1(c1,c2):
    p = position(c1)
    q = position(c2)
    diff = (q[0]-p[0],q[1]-p[1])
    output = ""
    if (diff[0] > 0):
        output += 'D'*abs(diff[0])
    if (diff[0] < 0):
        output += 'U'*abs(diff[0])
    if (diff[1] > 0):
        output += 'R'*abs(diff[1])
    if (diff[1] < 0):
        output += 'L'*abs(diff[1])
    output += '!'
    return output

def seq_2(c1,c2):
    p = position(c1)
    q = position(c2)
    diff = (q[0]-p[0],q[1]-p[1])
    output = ""
    if (diff[1] > 0):
        output += 'R'*abs(diff[1])
    if (diff[1] < 0):
        output += 'L'*abs(diff[1])
    if (diff[0] > 0):
        output += 'D'*abs(diff[0])
    if (diff[0] < 0):
        output += 'U'*abs(diff[0])
    output += '!'
    return output

class Solution(object):


    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        target = 'a' + target
        output = ""
        for i in range(len(target)-1):
            if target[i+1] != 'z':
                output += seq_1(target[i],target[i+1])
            else:
                output += seq_2(target[i],target[i+1])
        return output
