class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2

        merged.sort()

        total = len(merged)

        if total % 2 == 1:
            return float(merged[total // 2])

        else:
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return float((middle1 + middle2) / 2)


## OR


class solution:
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0

        for count in range(0, (n + m) // 2 + 1):
            m2 = m1
            if (
                i < n and j < m
            ):  # if both list have not fully tranversed, assign m1 to the smaller number
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j = j + 1
                else:
                    m1 = nums1[i]
                    i = i + 1
            elif i < n:  # if list 1 have not fully tranversed
                m1 = nums1[i]
                i = i + 1
            else:  # if list 2 have not fully tranversed
                m1 = nums2[j]
                j = j + 1

        if (n + m) % 2 == 1:
            return float(m1)
        else:
            ans = float(m1) + float(m2)
            return ans / 2.0


## Explanation for 2 pointer method,

# i and j are pointers for each num list
# m1 stores the most recent number
# m2 stores the second most recent number
