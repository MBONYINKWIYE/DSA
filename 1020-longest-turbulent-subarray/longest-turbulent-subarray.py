class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 1
        max_len = 1
        
        while right < len(arr):
            if arr[right-1] == arr[right]:
                max_len = max(max_len, 1)
                left = right
            elif right + 1 < len(arr) and not (arr[right-1] < arr[right] > arr[right+1]) and not (arr[right-1] > arr[right] < arr[right+1]):
                max_len = max(right - left + 1, max_len)
                left = right
            else:
                max_len = max(right-left+1, max_len)
            right += 1
        return max_len