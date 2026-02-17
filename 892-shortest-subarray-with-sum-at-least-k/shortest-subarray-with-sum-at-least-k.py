class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_len = float('inf')
        isokay = False
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            
        dq = deque()
        
        for right in range(n + 1):
            while dq and prefix_sum[right] - prefix_sum[dq[0]] >= k:
                isokay = True
                left = dq.popleft()
                min_len = min(min_len, right - left)
            
            while dq and prefix_sum[right] <= prefix_sum[dq[-1]]:
                dq.pop()
                
            dq.append(right)
            
        if not isokay:
            return -1
        return min_len