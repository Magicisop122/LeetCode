class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if (m * k) > len(bloomDay):

            return - 1

        l, r = min(bloomDay), max(bloomDay)
        res = -1

        while l <= r:
            mid = l + (r - l) // 2

            bouquets = 0
            flowers = 0
            for b in bloomDay:
                if b <= mid:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

        
        