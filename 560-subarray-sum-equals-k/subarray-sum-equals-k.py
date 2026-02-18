class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        res = 0
        count = defaultdict(int)
        count = {0 : 1}

        for n in nums:
            total += n
            diff = total - k

            res += count.get(diff, 0)
            count[total] = 1 + count.get(total, 0)          
        return res
            