class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = sorted(nums1 + nums2)
        
        median = statistics.median(merged)
        return median
        