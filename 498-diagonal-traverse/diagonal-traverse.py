class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dict1 = {}
        ans = []
        for row_idx in range(len(mat)):
            for col_idx in range(len(mat[row_idx])):
                key = col_idx + row_idx
                if key not in dict1:
                    dict1[key] = []
                dict1[key].append(mat[row_idx][col_idx])
        for row in dict1.items():
            if row[0] % 2 == 0:
                [ans.append(col) for col in row[1][::-1]]
            else:
                [ans.append(col) for col in row[1]]
        return ans