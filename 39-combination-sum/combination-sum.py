class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def combination(idx, subarr, total):
            if total == target:
                res.append(subarr[:])
                return
            if  idx >= len(candidates):
                return
            if total > target:
                return
            
            subarr.append(candidates[idx])
            combination(idx, subarr, total + candidates[idx])
            subarr.pop()
            combination(idx+1, subarr, total)

            return res

        return combination(0, [], 0)