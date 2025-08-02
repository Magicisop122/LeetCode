class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # linear search O(n)

        # for i in range(0, len(nums) - 1, 2):
        #     if nums[i] != nums[i + 1]:
        #         return nums[i]

        # return nums[-1]

        # binary search
        n = len(nums)

        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        l, r = 1, n - 2

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            else:
                # we have to check whether element is on right or left

                if mid % 2 == 0:
                    # means its even
                    if nums[mid] == nums[mid - 1]:
                        r = mid - 1
                    else:
                        l = mid + 1
                
                else:
                    # its odd
                    if nums[mid] == nums[mid - 1]:
                        l = mid + 1
                    else:
                        r = mid - 1
            
        

        