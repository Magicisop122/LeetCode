class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l, r = 0, 1

        while r <= len(nums) - 1:
            if nums[r] != nums[l]:
                nums[l + 1] = nums[r]
                l += 1
            r += 1

        return l + 1