class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ''
        if len(strs) == 0: return output
        while (len(strs[0]) != 0):
            proposal = strs[0][0]
            for i in range(len(strs)):
                if (len(strs[i]) == 0):
                    return output
                if (strs[i][0] != proposal):
                    return output
                strs[i] = strs[i][1:]
            output = output + proposal
        return output
        
