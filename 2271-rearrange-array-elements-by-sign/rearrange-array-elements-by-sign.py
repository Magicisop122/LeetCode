class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # pos = [n for n in nums if n > 0]
        # neg = [n for n in nums if n < 0]
        # res = []

        # for i in range(len(neg)):
        #     res.append(pos[i])
        #     res.append(neg[i])

        # return res

        res = [0] * len(nums)
        l, r = 0, 1

        for i in range(len(nums)):
            if nums[i] > 0:
                res[l] = nums[i]
                l += 2
            else:
                res[r] = nums[i]
                r += 2
        return res

