class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # l, r = 0, len(nums) - 1

        # for i in range(len(nums)):
        #     mid = (l + r) // 2

        #     if target < nums[mid]:
        #         r = mid - 1
        #     elif target > nums[mid]:
        #         l = mid + 1
        #     else:
        #         return mid

        # return -1
        

        def helper(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(mid + 1, right)
            else:
                return helper(left, mid - 1)
        return helper(0, len(nums) - 1)
    