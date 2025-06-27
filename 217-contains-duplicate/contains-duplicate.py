class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # hashset = set()

        # for i in nums:
        #     if i in hashset:
        #         return True
        #     hashset.add(i)

        # return False
        
        # more optimal

        arr = set(nums)

        if len(arr) != len(nums):
            return True
        else:
            return False

