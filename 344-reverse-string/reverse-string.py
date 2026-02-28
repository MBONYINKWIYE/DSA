class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(left, r):
            if left >= r:
                return 
            s[left], s[r] = s[r], s[left]

            rev(left + 1, r - 1)
        rev(0, len(s)-1)
