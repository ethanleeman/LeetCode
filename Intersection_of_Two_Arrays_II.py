class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        answer = []
        i = 0
        j = 0
        while (i < len(nums1) and j < len(nums2)):
            print(i)
            print(nums1[i])
            print(j)
            print(nums2[j])
            print("\n")
            if (nums1[i] == nums2[j]):
                answer.append(nums1[i])
                i += 1
                j += 1
            elif (nums1[i] < nums2[j]):
                i += 1
            else:
                j += 1
        return answer
