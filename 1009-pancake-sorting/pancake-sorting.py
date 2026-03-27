class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans =[]
        for i in range(len(arr),0,-1):
            max_idx = arr.index(max(arr[:i]))

            if max_idx == i - 1: continue

            if max_idx !=0:
                arr[:max_idx+1] = arr[:max_idx+1][::-1]
                ans.append(max_idx+1)

            arr[:i] = arr[:i][::-1]
            ans.append(i)
            
        return ans