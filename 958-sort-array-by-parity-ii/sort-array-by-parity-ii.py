class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        while right < len(nums) and left < len(nums):
            if nums[right] % 2 != 0:
                right += 2 
            elif nums[left] % 2 == 0:
                left += 2
            else:
                nums[left],nums[right] = nums[right],nums[left]
                # left += 2
                # right += 2
        return nums