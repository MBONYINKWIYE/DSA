class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        temp = 0
        for col in range(n):
            for row in range(col + 1,n):
              matrix[col][row] , matrix[row][col] = matrix[row][col], matrix[col][row]
        for i in range(n):
            matrix[i].reverse()