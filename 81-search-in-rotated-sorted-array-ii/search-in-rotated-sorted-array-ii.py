class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # linear search

        res = False

        for i in range(len(nums)):
            if nums[i] == target:
                res = True

        return res
        