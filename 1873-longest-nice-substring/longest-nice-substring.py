class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        sub_set = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in sub_set:
                res1 = self.longestNiceSubstring(s[:i])
                res2 = self.longestNiceSubstring(s[i + 1:])

                if len(res2) > len(res1):
                    return res2
                else:
                    return res1
        return s