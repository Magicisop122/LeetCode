class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        new = set(nums)
        longest = 0

        for n in new:
            if n - 1 not in new:
                curr = n
                streak = 1
                while curr + 1 in new:
                    curr += 1
                    streak += 1
                
                longest = max(longest, streak)

        return longest