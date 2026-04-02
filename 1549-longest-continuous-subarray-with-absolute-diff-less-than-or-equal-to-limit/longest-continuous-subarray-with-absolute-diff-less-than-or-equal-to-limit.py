from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mini_idx = deque()
        max_idx = deque()
        max_len = 0
        left = 0
        
        for right in range(len(nums)):

            while max_idx and nums[max_idx[-1]] <= nums[right]:
                max_idx.pop()
            max_idx.append(right)

            while mini_idx and nums[mini_idx[-1]] >= nums[right]:
                mini_idx.pop()
            mini_idx.append(right)

            while nums[max_idx[0]] - nums[mini_idx[0]] > limit:
                if max_idx[0] == left:
                    max_idx.popleft()
                if mini_idx[0] == left:
                    mini_idx.popleft()
                left += 1
                
            max_len = max(max_len, right - left + 1)

        return max_len
            