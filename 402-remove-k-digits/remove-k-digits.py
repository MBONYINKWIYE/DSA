import sys
sys.set_int_max_str_digits(10**6)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:

            while stack and n < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            else:
                stack.append(n)
        while k and stack:
            stack.pop()
            k -= 1

        if stack:
            res = int("".join(stack))
            return f"{res}"
        else:
            return f"{len(stack)}"