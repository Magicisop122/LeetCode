class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # hashset = set()

        # for i in nums:
        #     if i in hashset:
        #         return True
        #     hashset.add(i)
        # return False
        

        arr = set(nums)

        if len(nums) != len(arr):
            return True
        else:
            return False