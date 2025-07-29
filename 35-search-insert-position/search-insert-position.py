class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)
        low, high = 0, n - 1
        res = n

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] >= target:
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res
                

        
        