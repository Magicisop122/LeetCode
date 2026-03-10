class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ROWS, COLS = len(image), len(image[0])
        visit = set()
        q = deque()
        startColor = image[sr][sc]

        if startColor == color:
            return image
        
        q.append((sr, sc))
        visit.add((sr, sc))

        while q:
            r, c = q.popleft()
            image[r][c] = color

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            for dr, dc in neighbors:
                if ((r + dr) < 0 or (c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or
                    image[r + dr][c + dc] != startColor):
                    continue
                q.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
            
        return image

      
        

