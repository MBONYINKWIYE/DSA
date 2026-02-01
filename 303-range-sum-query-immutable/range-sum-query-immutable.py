class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = nums
        prefixSum = [0]* (len(self.prefix))
        total = 0
        for i in range(len(self.prefix)): 
            total += self.prefix[i]
            prefixSum[i] = total
        print(prefixSum)
        for i in range(len(prefixSum)):
            self.prefix[i] = prefixSum[i]

    def sumRange(self, left: int, right: int) -> int:
        # return self.prefix
        if left > 0:
            return (self.prefix[right] - self.prefix[left -1])
        else:
            return self.prefix[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)