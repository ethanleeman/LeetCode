def binary_list(n:int) -> List[int]:
    if n == 0:
        return [0]

    answer = []
    curr = abs(n)
    while (curr > 0):
        answer.append(curr % 2)
        curr = curr // 2
    return answer

class Solution:
    def myPow(self, x: float, n: int) -> float:
        n_to_binary = binary_list(n)

        if n == 0:
            return 1

        if n > 0:
            answer = 1.0
            curr = x
            for bit in n_to_binary:
                if bit == 1:
                    answer *= curr
                curr *= curr
            return answer
        if n < 0:
            answer = 1.0
            curr = x
            for bit in n_to_binary:
                if bit == 1:
                    answer /= curr
                curr *= curr
            return answer
            
