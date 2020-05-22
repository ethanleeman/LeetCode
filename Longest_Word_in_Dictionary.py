

class Solution(object):

    @staticmethod
    def isCandidate(dic, w):
        for i in range(1,len(w)):
            if (w[0:i] not in dic.keys()):
                return False
        return True

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        words.sort()
        d = {}
        for w in words:
            d[w] = False
        mx = ""
        mxlen = 0
        for w in words:
            if (len(w) == 1):
                d[w] = True
            else:
                if (w[0:-1] in d.keys()):
                    if (d[w[0:-1]] == True):
                        d[w] = True
        for w in words:
            if (d[w] == True):
                if (len(w) > mxlen):
                    mx = w
                    mxlen = len(w)
        return mx

               
