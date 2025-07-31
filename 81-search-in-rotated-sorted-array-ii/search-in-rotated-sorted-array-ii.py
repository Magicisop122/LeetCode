class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # linear search

        # res = False

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res = True

        # return res

        # 
        nums.sort()
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        