class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # brute force

        ROWS, COLS = len(matrix), len(matrix[0])
        res = False

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == target:
                    res = True

        return res
        