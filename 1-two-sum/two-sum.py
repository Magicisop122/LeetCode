class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}   # we are going to map value : index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i   #update the hashmap

        return     
        