class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force
        # n = len(nums)

        # k = k % n

        # temp = nums[-k:]

        # for i in range(n-k-1, -1, -1):
        #     nums[i + k] = nums[i]

        # for i in range(k):
        #     nums[i] = temp[i]

        # optimal way by reversing split parts

        n = len(nums)
        k = k % n

        def rotate(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        rotate(0, n-k-1)

        rotate(n-k, n-1)

        rotate(0, n-1)


        