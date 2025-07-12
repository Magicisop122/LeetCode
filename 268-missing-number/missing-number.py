class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # brute force

        # for i in range(len(nums) + 1):
        #     if i not in nums:
        #         return i

        # better

        # hashset = set(nums)

        # for i in range(len(nums) + 1):
        #     if i not in hashset:
        #         return i

        # optimal

        # sum solution

        # n = len(nums)
        # total = n * (n + 1) // 2

        # actual_sum = sum(nums)

        # return total - actual_sum

        # XOR solution

        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])

        return res 