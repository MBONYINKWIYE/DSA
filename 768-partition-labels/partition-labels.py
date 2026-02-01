class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        result = []
        left = 0
        right = 0

        for i, char in enumerate(s):
            last_occurrence[char] = i
        print(last_occurrence)
        for i, char in enumerate(s):
            right = max(right, last_occurrence[char])
            print(right)
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        
        return result