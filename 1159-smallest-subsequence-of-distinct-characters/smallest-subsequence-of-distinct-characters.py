class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        char = defaultdict(lambda: 0)

        for i in range(len(s)):
            char[s[i]] += 1
        
        for idx, c in enumerate(s):
            char[c] -= 1
            
            if c in stack:
                continue

            while stack and c < stack[-1] and char[stack[-1]] > 0:
                stack.pop()
            
            stack.append(c)
        
        return "".join(stack)