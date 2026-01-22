class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,min_len = 0,float('inf')
        sub_arr = []
        curr_sum = 0
        for right in range(0,len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                if left <= right:
                    min_len = min(min_len, right-left+1)
                    curr_sum -= nums[left]
                    left += 1

            print(min_len)
        if min_len == float('inf'):
            return 0
        else:
            return min_len
            