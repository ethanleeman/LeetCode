class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        answer = []
        while (i > -1):
            answer.insert(0,(digits[i]+carry) % 10)
            if (digits[i]+carry == 10): carry = 1
            else: carry = 0
            i -= 1
        if (carry == 1):
            answer.insert(0,1)
        return answer
        
