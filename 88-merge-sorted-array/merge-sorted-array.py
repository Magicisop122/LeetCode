class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m] + nums2[:n]
        temp.sort()

        for i in range(m + n):
            nums1[i] = temp[i]