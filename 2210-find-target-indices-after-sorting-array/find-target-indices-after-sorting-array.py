class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j + 1],nums[j] = nums[j],nums[j + 1]
            # if target == nums[i]:
            #     result.append(i)
        # after getting sorted array we gonna retrieve the index of our target
        for i, val in enumerate(nums):
            if val == target:
                result.append(i)
        print(nums)
        return result