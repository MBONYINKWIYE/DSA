class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            elif nums1[i] >= nums2[j]:
                result.append(nums2[j])
                j += 1
        # We need to check the element out of bounds for every array because we don't
        #know which will be out of bounds
        while i < m:
            result.append(nums1[i])
            i += 1
        while j < n:
            result.append(nums2[j])
            j += 1
        for i in range(m+n):
            nums1[i] = result[i]