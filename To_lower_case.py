class Solution:
    def toLowerCase(self, str: str) -> str:
        output = ""
        for c in str:
            if (ord('Z') >= ord(c) and ord(c) >= ord('A')):
                output = output + chr(ord('a') + ord(c) - ord('A'))
            else:
                output = output + c
        return output

        
