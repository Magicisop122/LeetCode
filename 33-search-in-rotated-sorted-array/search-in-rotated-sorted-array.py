class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # linear search 

        res = -1

        for i in range(len(nums)):
            if nums[i] == target:
                res = i

        return res

        # binary search
        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            
            # left sorted
            elif nums[mid] >= nums[l]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # right sorted
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1

                else:
                    r = mid - 1

        return res                



            