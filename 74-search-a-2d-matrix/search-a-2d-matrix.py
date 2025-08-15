class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # ROWS, COLS = len(matrix), len(matrix[0])

        # res = False

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == target:
        #             res = True

        # return res

        # binary search
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            mid = low + (high - low) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
