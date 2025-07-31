class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # first, last = -1, -1

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         if first == -1:
        #             first = i
        #         last = i

        # return [first, last]

        # binary 

        # [5,7,7,8,8,10]
        # l = 0 r = 5 mid = 2
        # l = 3 r = 5 mid = 4 lb = 4 index
        # l = 5 r = 5 mid = 5
        
        lb = -1
        ub = -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                lb = mid
                r = mid - 1
        

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                ub = mid
                l = mid + 1
        
        return [lb, ub]



        