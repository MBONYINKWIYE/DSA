class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        prefix_sum = 0
        res = 0
        count[0] = 1

        for n in nums:
            prefix_sum += n
            remainder = prefix_sum % k

            res += count[remainder]
            count[remainder] += 1

        return res