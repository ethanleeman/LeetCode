class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        for i in range(len(groupSizes)):
            if (groupSizes[i] == 0):
                continue

            addList = [i]
            size = groupSizes[i]
            groupSizes[i] = 0
            counter = size - 1
            for j in range(i+1,len(groupSizes)):
                if (counter == 0):
                    break
                if (groupSizes[j] == size):
                    counter -= 1
                    addList.append(j)
                    groupSizes[j] = 0


            answer.append(addList)
        return answer
            
