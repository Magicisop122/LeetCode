class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        

        hashmap = {}
        final = []

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        for n in hashmap:
            if hashmap[n] > (len(nums) // 3):
                final.append(n)

        return final
                
        