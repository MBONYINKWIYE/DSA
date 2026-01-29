class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            runningSum.append(total)
        return runningSum