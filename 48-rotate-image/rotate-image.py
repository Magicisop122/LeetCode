class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0(n * n) solution with extra 0(n * n) memory

        # n = len(matrix)
        # rotated = [[0] * n for _ in range(n)]

        # for i in range(n):
        #     for j in range(n):
        #         rotated[j][n - 1 - i] = matrix[i][j]

        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = rotated[i][j]

        # optimal solution without extra memory

        n = len(matrix)
        
        # first lets transpose the matrix

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse the rows

        for i in range(n):
            matrix[i].reverse()

        