class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # brute force

        # if len(nums) == 1:
        #     return 0

        # if nums[0] > nums[1]:
        #     return 0

        # if nums[len(nums) - 1] > nums[len(nums) - 2]:
        #     return len(nums) - 1

        # for i in range(1, len(nums) - 1):
        #     if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        #         return i

        # binary search

        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        
        l, r = 1, n - 2

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            else:
                if nums[mid] > nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        