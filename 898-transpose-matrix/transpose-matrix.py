class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for row_idx in range(len(matrix[0])):
            result = []
            for col_idx in range(len(matrix)):
               result.append(matrix[col_idx][row_idx])
            ans.append(result)  
        return ans