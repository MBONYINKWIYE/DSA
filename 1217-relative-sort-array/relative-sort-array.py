class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        for i in range(len(arr2)):
            for j in arr1:
                if j == arr2[i]:
                    result.append(j)
        ans = []
        for n in range(len(arr1)):
            if arr1[n] not in arr2:
                ans.append(arr1[n])
                ans.sort()
        result.extend(ans)
        return result
