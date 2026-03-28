class Solution:
    def subsetsWithDup(self, nums: List[int]) :
        nums.sort()
        ans = []
        path = []
        def backtrack(i, path, length):
            if i == length: #and path not in ans:
                ans.append(path[:])
                return

            path.append(nums[i])
            backtrack(i + 1, path, length)
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1, path, length)   
        backtrack(0, [], len(nums))
        return ans