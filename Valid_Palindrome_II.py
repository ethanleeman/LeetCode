def isPalindrome(s:str) -> bool:
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        while (len(s) > 1):
            if s[0] == s[len(s)-1]:
                s = s[1:-1]
            else:
                return isPalindrome(s[1:]) or isPalindrome(s[:-1])
        return True

            
