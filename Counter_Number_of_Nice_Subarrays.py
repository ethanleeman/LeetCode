class Solution(object):
    def numberOfSubarrays(self, nums, k):

        # indexes of the odd elements
        L = []
        for i in range(len(nums)):
            if ((nums[i] % 2) == 1):
                L.append(i)

        if (k > len(L)):
            return 0

        # need every odd number
        # so product of how many even numbers on each side +1
        if (k == len(L)):
            return (L[0]+1)*(len(nums)-L[k-1])


        # if not every odd number
        # do the same thing moving across the array L
        counter = 0

        # very beginning, using the first odd number
        counter += (L[0]+1)*(L[k]-L[k-1])

        # middle
        for i in range(1,len(L)-k):
            counter += (L[i]-L[i-1])*(L[i+k]-L[i+k-1])

        # very end, using the last odd number
        counter += (L[-k]-L[-k-1])*(len(nums)-L[-1])

        return counter
