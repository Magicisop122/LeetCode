class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # time complexity will be O(n * n)
        # if we are considering the output space then it will be 

        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res