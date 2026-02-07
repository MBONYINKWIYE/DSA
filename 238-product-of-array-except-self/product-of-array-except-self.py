class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
            print(prefix)  
        for l in range(len(nums)-1,-1,-1):
            ans[l] *= suffix
            suffix *= nums[l]
            print(suffix)
        return ans