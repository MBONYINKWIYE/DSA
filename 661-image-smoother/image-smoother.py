class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        columns = len(img[0])
        rows = len(img)
        ans = [[0] * columns for i in range(rows)]
        for row_idx in range(len(img)):
            for col_idx in range(len(img[row_idx])):
                total, count = 0, 0
                for i in range(row_idx -1, row_idx +2):
                    for j in range(col_idx - 1, col_idx + 2):
                        if  i < 0 or i >= rows or j < 0 or j >= columns:
                            continue
                        total += img[i][j]
                        count += 1
                average = total // count
                ans[row_idx][col_idx] = average

        return ans