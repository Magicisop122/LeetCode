class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        r = [0] * m
        c = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r[i] = 1
                    c[j] = 1

        # second pass

        for i in range(m):
            for j in range(n):
                if r[i] == 1 or c[j] == 1:
                    matrix[i][j] = 0
            

