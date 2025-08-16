class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # brute force

        # ROWS, COLS = len(matrix), len(matrix[0])
        # res = False

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if matrix[i][j] == target:
        #             res = True

        # return res

        # better solution

        def binarySearch(nums, target):
            n = len(nums)
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False

        m = len(matrix)
        
        for i in range(m):
            flag = binarySearch(matrix[i], target)
            if flag:
                return True
            
        return False