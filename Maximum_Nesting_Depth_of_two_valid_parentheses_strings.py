class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:

        ## Number of left parenthesis to close
        A = 0
        B = 0

        answer = []
        for s in seq:
            if s == '(':

                ## Add left parenthesis to smaller value,
                ## greedily makes depth as small as can be
                if B < A:
                    B += 1
                    answer.append(1)
                else:
                    A += 1
                    answer.append(0)
            else:

                ## remove a left parenthesis from larger value
                if B < A:
                    A -= 1
                    answer.append(0)
                else:
                    B -= 1
                    answer.append(1)

        return answer
