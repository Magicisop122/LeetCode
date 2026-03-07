class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # brute force

        # res = float('-inf')
        

        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         res = max(res, total)
        # return res

        # # kadane's algo

        maxSum = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum
        