class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # brute force O(n^2) solution
        intervals.sort()
        n = len(intervals)
        res = []

        for i in range(n):
            start, end = intervals[i]

            if not res or res[-1][1] < start:
                res.append([start, end])
            
            else:
                res[-1][1] = max(res[-1][1], end)

        return res