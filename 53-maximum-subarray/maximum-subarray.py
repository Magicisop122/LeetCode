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

        curSum = 0
        res = float('-inf')

        for i in range(len(nums)):
            curSum += nums[i]
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0

        return res 

        