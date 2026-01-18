class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n =len(names)
        swap = False
        while n > 0:
            for j in range(n - 1):
                if heights[j] < heights[j + 1]:
                    swap = True
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
            n -= 1
            if not swap:
                return names
                break
        return names
