class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if matrix[m-1][n-1] < target:
            return False
        for i in matrix:
            if i[n - 1] < target:
                continue
            if target in i:
                return True
        return False
        