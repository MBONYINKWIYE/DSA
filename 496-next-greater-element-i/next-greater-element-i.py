class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mono = defaultdict(lambda: -1)

        for idx, num in enumerate(nums2):
            while stack and nums2[idx] > nums2[stack[-1]]:
                top = stack.pop()
                mono[nums2[top]] = num
            mono[num] = -1
            stack.append(idx)
        
        ans = []
        for num in nums1:
            ans.append(mono[num])
        return ans