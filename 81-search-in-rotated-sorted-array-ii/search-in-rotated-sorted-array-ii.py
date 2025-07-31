class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # linear search

        # res = False

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res = True

        # return res

        # 
        # nums.sort()
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if nums[mid] == target:
        #         return True
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        
        # return False

        # binary

        

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
                
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]:
                if target <= nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
                
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                
        return False
        