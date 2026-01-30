class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix)+1, len(matrix[0])+1
        self.prefix = [[0] * cols for row in range(rows)]

        for r in range(rows -1):
            for c in range(cols -1):
                self.prefix[r+1][c+1] = (
                    self.prefix[r][c+1] + 
                    self.prefix[r+1][c] - 
                    self.prefix[r][c] + 
                    matrix[r][c])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r2, c2 = row2+1, col2 +1
        r1, c1 = row1, col1
        return (
            self.prefix[r2][c2] - 
            self.prefix[r2][c1] -
            self.prefix[r1][c2] +
            self.prefix[r1][c1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)