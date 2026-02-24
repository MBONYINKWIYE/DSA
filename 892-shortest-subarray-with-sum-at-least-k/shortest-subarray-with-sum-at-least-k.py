class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        from collections import deque
        n = len(nums)
        min_len = float('inf')
        isokay = False
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            
        queue = deque()
        
        for right in range(n + 1):
            while queue and prefix_sum[right] - prefix_sum[queue[0]] >= k:
                isokay = True
                left = queue.popleft()
                min_len = min(min_len, right - left)
            
            while queue and prefix_sum[right] <= prefix_sum[queue[-1]]:
                queue.pop()
                
            queue.append(right)
            
        if isokay:
            return min_len
        return -1