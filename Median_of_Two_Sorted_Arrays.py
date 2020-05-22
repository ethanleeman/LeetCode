def findMedian(nums1: List[int], start: int, end: int)  -> float:
        length = end - start
        if (length % 2 != 0) :
            return nums1[start + int(length/2)]
        return (nums1[int(start + length/2-1)] + nums1[int(start + length/2)])/ 2.0

def findMedianSortedArrays(nums1: List[int], start1: int, end1: int, nums2: List[int], start2: int, end2:int) -> float:
        length1 = end1 - start1
        length2 = end2 - start2
        if (length1 > length2 ): return findMedianSortedArrays(nums2, start2, end2, nums1, start1, end1)
        if (length1 is 0): return findMedian(nums2, start2, end2)
        if (length1 is 1) :
            if (length2 is 1) : return (nums1[start1] + nums2[start2])/2.0
            if (length2 % 2 is 0) :
                if (nums1[start1] < nums2[start2+int(length2/2)-1]): return nums2[start2+int(length2/2)-1]
                if (nums1[start1] > nums2[start2+int(length2/2)]): return nums2[start2+int(length2/2)]
                return nums1[start1]

            if (nums1[start1] < nums2[start2 + int(length2/2) -1]): return (nums2[start2 + int(length2/2) -1] + nums2[start2 + int(length2/2) ]) /2.0
            if (nums1[start1] > nums2[start2 + int(length2/2)+1]): return (nums2[start2 + int(length2/2)] + nums2[start2+ int(length2/2) +1]) /2.0
            return (nums1[start1] + nums2[start2 + int(length2/2)])/2.0

        if (length1 < length2 / 3) :
            return findMedianSortedArrays(nums1, start1, end1, nums2, start2+int(length2/3), end2-int(length2/3));

        if (nums1[start1+int(length1/2)-1] > nums2[start2+int(length1/2)-1]) :
            if (nums1[end1-int(length1/2)] > nums2[end2-int(length1/2)]) :
                return findMedianSortedArrays(nums1, start1, end1-int(length1/2), nums2, start2+int(length1/2), end2)
            return findMedianSortedArrays(nums1, start1, end1, nums2, start2+int(length1/2), end2-int(length1/2))

        if (nums1[end1-int(length1/2)] > nums2[end2-int(length1/2)]) :
            return findMedianSortedArrays(nums1, start1+int(length1/2), end1-int(length1/2), nums2, start2, end2)
        return findMedianSortedArrays(nums1, start1+int(length1/2), end1, nums2, start2, end2-int(length1/2))




class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return findMedianSortedArrays(nums1, 0, len(nums1), nums2, 0, len(nums2))
