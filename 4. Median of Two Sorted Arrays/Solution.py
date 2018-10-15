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


          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]



'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) > len(nums2):
            tmp_array = nums1
            nums1 = nums2
            nums2 =tmp_array
        
        m, n = len(nums1), len(nums2)
        imin = 0
        imax = m
        half_len = (m + n + 1) // 2

        i, j = 0, 0
        numI, numII = 0, 0

        while (imin <= imax):
            i = (imin + imax) // 2
            j = half_len - i
            if j > 0 and i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and j < n and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    numI = nums2[j-1]
                elif j == 0:
                    numI = nums1[i-1]
                else:
                    numI = max(nums1[i-1], nums2[j-1])
                break
        
        if (m + n) % 2 == 1:
            return numI
        
        if i == m:
            numII = nums2[j]
        elif j == n:
            numII = nums1[i]
        else:
            numII = min(nums1[i], nums2[j])
        
        return (numI + numII) / 2.0

        


