class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # extra memory solution hashmap

        # hashmap = {}
        # final = []

        # for n in nums:
        #     if n in hashmap:
        #         hashmap[n] += 1
        #     else:
        #         hashmap[n] = 1

        # for n in hashmap:
        #     if hashmap[n] > (len(nums) // 3):
        #         final.append(n)

        # return final

        # boyer moore

        if not nums:
            return []

        ele1 = ele2 = None
        cnt1 = cnt2 = 0

        for n in nums:
            if n == ele1:
                cnt1 += 1
            elif n == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele1, cnt1 = n, 1
            elif cnt2 == 0:
                ele2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        res = []

        for ele in [ele1, ele2]:
            if nums.count(ele) > len(nums) // 3:
                res.append(ele)

        return res        