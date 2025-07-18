class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # optimal approach with prefix sum O(n)

        hashmap = {0:1}
        prefixSum = 0
        cnt = 0

        for n in nums:
            prefixSum += n

            if (prefixSum - k) in hashmap:
                cnt += hashmap[prefixSum - k]

            if prefixSum in hashmap:
                hashmap[prefixSum] += 1
            else:
                hashmap[prefixSum] = 1

        return cnt
            

       

        

        
        