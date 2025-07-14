class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # better approach(extra space)

        # hashmap = {}
        # majority = len(nums) // 2

        # for n in nums:
        #     if n in hashmap:
        #         hashmap[n] += 1
        #     else:
        #         hashmap[n] = 1
        
        #     if hashmap[n] > majority:
        #         return n

        # optimal solution(moore's voting algo)

        ele = nums[0]

        cnt = 1

        for i in range(1, len(nums)):
            if ele == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                
            if cnt == 0:
                ele = nums[i + 1]

        return ele



        
        
        