class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l, r = 1, max(nums)

        res = r

        while l <= r:
            mid = l + (r - l) // 2

            total = 0

            for n in nums:
                total += math.ceil(n / mid)

            if total <= threshold:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res



        
        