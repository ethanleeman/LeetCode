double findMedian(int* nums1, int start, int end) {
        int length = end - start;
        if (length % 2 != 0) {
            return nums1[start + length/2];
            }
        return (nums1[start + length/2-1] + nums1[start + length/2])/ 2.0;
        }

double findMedianSortedArrays1(int* nums1, int start1, int end1, int* nums2, int start2, int end2) {
        int length1 = end1 - start1;
        int length2 = end2 - start2;
        if (length1 > length2 ) return findMedianSortedArrays1(nums2, start2, end2, nums1, start1, end1);
        if (length1 == 0) return findMedian(nums2, start2, end2);
        if (length1 == 1) {
            if (length2 == 1) { return (nums1[start1] + nums2[start2])/2.0;}
            if (length2 % 2 == 0) {
                if (nums1[start1] < nums2[start2+length2/2-1]) return nums2[start2+length2/2-1];
                if (nums1[start1] > nums2[start2+length2/2]) return nums2[start2+length2/2];
                return nums1[start1];
            }
            if (nums1[start1] < nums2[start2 + length2/2 -1]) return (nums2[start2 + length2/2 -1] + nums2[start2 + length2/2 ]) /2.0;
            if (nums1[start1] > nums2[start2 + length2/2+1]) return (nums2[start2 + length2/2] + nums2[start2 + length2/2 +1]) /2.0;
            return (nums1[start1] + nums2[start2 + length2/2])/2.0;
        }

        if (length1 < length2 / 3) {
                return findMedianSortedArrays1(nums1, start1, end1, nums2, start2+length2/3, end2-length2/3);

        }

        if (nums1[start1+length1/2-1] > nums2[start2+length1/2-1]) {
            if (nums1[end1-length1/2] > nums2[end2-length1/2]) {
                return findMedianSortedArrays1(nums1, start1, end1-length1/2, nums2, start2+length1/2, end2);
                }
                return findMedianSortedArrays1(nums1, start1, end1, nums2, start2+length1/2, end2-length1/2);
            }
        if (nums1[end1-length1/2] > nums2[end2-length1/2]) {
            return findMedianSortedArrays1(nums1, start1+length1/2, end1-length1/2, nums2, start2, end2);
                }
        return findMedianSortedArrays1(nums1, start1+length1/2, end1, nums2, start2, end2-length1/2);

    }



double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
    return findMedianSortedArrays1(nums1, 0, nums1Size, nums2, 0, nums2Size);
}
