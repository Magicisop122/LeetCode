class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # observation based 0(n)
        n = len(nums)

        prefix = 1
        suffix = 1
        maximumProduct = float('-inf')

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            prefix = prefix * nums[i]
            suffix = suffix * nums[n - i - 1]

            maximumProduct = max(maximumProduct, max(prefix, suffix))

        return maximumProduct

        