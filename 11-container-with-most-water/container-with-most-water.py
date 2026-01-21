class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        area = []
        while left <= right:
            if height[left] < height[right]:
                area.append(height[left] * (right - left))
                left += 1
            else:
                area.append(height[right] * (right - left))
                right -= 1
        print(area)
        return max(area)