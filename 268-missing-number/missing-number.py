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

        n = len(nums)
        total = n * (n + 1) // 2

        actual_sum = sum(nums)

        return total - actual_sum