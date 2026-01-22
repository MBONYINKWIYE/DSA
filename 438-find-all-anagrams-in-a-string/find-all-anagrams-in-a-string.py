class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        left, result = 0,[]
        curr_anag = Counter(p)
        for right in range(len(p),len(s)+1):
            window = Counter(s[left:right])
            if curr_anag ==  window:
                result.append(left)
            left += 1
        
        return result