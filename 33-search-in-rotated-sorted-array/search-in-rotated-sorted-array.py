class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            # check if we are in left sorted or right sorted
            if nums[mid] >= nums[l]:
                # we are in left sorted 
                if target <= nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                # we are in right sorted
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1