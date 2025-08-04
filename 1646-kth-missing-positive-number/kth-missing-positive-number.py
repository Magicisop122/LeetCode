class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        # for i in range(len(arr)):
        #     if arr[i] <= k:
        #         k += 1

        #     else:
        #         break
        # return k


        # binary search

        n = len(arr)

        l, r = 0, n - 1

        while l <= r:
            mid = l + (r - l) // 2

            missing = arr[mid] - (mid + 1)

            if missing < k:
                l = mid + 1
            else:
                r = mid - 1

        return l + k

