class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) /k

        max_sum = sum(nums[0:k])
        left = 0
        average = 0
        total = max_sum
        for right in range(k, len(nums)):
            total = total - nums[left] + nums[right] 
            print(total)
            if total > max_sum:
                max_sum = total
            average = max_sum / k
            left += 1
        return average
        