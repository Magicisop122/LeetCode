class Solution:
    def findMin(self, nums: List[int]) -> int:
        # res = nums[0]

        # for i in range(1, len(nums)):
        #     res = min(res, nums[i])

        # return res

        # binary search

        res = float(inf)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            # left sorted
            if nums[mid] >= nums[l]:
                res = min(res, nums[l])
                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid - 1

        return res
        