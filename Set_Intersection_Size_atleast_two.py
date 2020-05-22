def contains(n, interval):
    if n < interval[0]:
        return False
    if n > interval[1]:
        return False
    return True

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda interval: -interval[1] )

        amt = [0]*len(intervals)
        total = 0

        while len(intervals) > 0:
            #print(intervals)
            #print(amt)
            #print("\n")

            curr_interval = intervals.pop()
            curr_amt = amt.pop()
            if (curr_amt < 2):
                new_spot = curr_interval[1]
                curr_amt += 1
                total += 1
                for i in range(len(intervals)):
                    if contains(new_spot,intervals[i]):
                        intervals[i][0] = intervals[i][0] + 1
                        amt[i] += 1
                if curr_amt == 1:
                    intervals.append([curr_interval[0]+1,curr_interval[1]])
                    amt.append(curr_amt)

        #print(s)
        return total

        
