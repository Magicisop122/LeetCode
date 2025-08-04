class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = l + (r - l) // 2
            subArray = 1
            curSum = 0
            for n in nums:
                if curSum + n > mid:
                    subArray += 1
                    curSum = 0
                curSum += n

            if subArray <= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res



        