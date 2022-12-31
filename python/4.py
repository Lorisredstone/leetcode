from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we need to merge the two arrays
        # we need to find the median
        # we need to return the median
        merged:List[int] = []
        i:int = 0
        j:int = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        if len(merged) % 2 == 0:
            return (merged[len(merged)//2] + merged[len(merged)//2 - 1]) / 2
        else:
            return merged[len(merged)//2]