class Solution(object):
    def helper(self, S, i, L):
        if (i == len(S)):
            L.append(S)
            return
        if (S[i].isdigit()):
            self.helper(S,i+1,L)
        elif (S[i].isupper()):
            self.helper(S,i+1,L)
            self.helper(S[:i] + S[i].lower() + S[i+1:],i+1, L)
        elif (S[i].islower()):
            self.helper(S,i+1,L)
            self.helper(S[:i] + S[i].upper() + S[i+1:],i+1, L)
        return



    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L = []
        self.helper(S, 0, L)
        return L
