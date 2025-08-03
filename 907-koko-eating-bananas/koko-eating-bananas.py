class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low, high = 1, max(piles)

        result = high

        while low <= high:
            k = low + (high - low) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                result = min(result, k)
                high = k - 1
            else:
                low = k + 1

        return result


        