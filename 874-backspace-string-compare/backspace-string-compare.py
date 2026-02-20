class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #Let's use here a new function to maintain backspacing character 
        def final_string(s) -> str:
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack :
                    stack.pop()
            return stack
        return final_string(s) == final_string(t)

