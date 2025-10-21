class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # res = []

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             res = [i, j]

        # return res

        
        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i

        

        
        