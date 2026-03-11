class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = float('inf')

        while q:
            r, c = q.popleft()
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS):
                    if mat[nr][nc] > mat[r][c]:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr, nc))

        return mat

        
                

        


        