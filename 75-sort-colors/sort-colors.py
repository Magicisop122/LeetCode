class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # better solution than brute force
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for n in nums:
            if n == 0:
                cnt0 += 1
            elif n == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        
        for i in range(cnt0):
            nums[i] = 0
        
        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1

        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2

        return nums