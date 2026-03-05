class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []

        def level(Index):
            if Index == 0:
                return [1]
            prev_row = level(Index - 1)
            res = [1]
            for i in range(len(prev_row) - 1):
                res.append(prev_row[i] + prev_row[i + 1])
            res.append(1)
            return res
        return level(rowIndex)