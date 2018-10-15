'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        c = nums1 + nums2
        c = sorted(c)
        total_len = len(c)
        mid_idx_or_left_max_idx = int((total_len-1) / 2)
        if total_len % 2 == 0:
            return(c[mid_idx_or_left_max_idx] + c[mid_idx_or_left_max_idx + 1]) / 2
        else:
            return c[mid_idx_or_left_max_idx]   


