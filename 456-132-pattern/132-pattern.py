class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mini = float('-inf')
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < mini:
                return True
            while stack and stack[-1] < nums[i]:
                mini = stack.pop()

            stack.append(nums[i])
        return False