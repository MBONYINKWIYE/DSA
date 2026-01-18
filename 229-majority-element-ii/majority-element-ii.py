class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        n = len(nums)
        a = Counter(nums)
        majority_elements = []
        for i in a:
            if a[i] > n/3:
                majority_elements.append(i)
        return majority_elements
            
                
            

            