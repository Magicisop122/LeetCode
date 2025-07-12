class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # brute force
        # temp = [num for num in nums if num != 0]

        # for i in range(len(temp)):
        #     nums[i] = temp[i]

        # for i in range(len(temp), len(nums)):
        #     nums[i] = 0

        # optimal

        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1

        return nums


        