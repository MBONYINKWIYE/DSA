class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0]* (n + 1)
        accumulator = 0
        for l, r, d in shifts:
            if d != 0:
                prefix[l] += 1
                prefix[r + 1] -= 1
            else:
                prefix[l] -= 1
                prefix[r + 1] +=1
        
        for i in range(len(s)):
            accumulator += prefix[i]
            prefix[i] = accumulator

        result = ""
        for idx, char in enumerate(s):
            temp = (ord(char) - ord('a') + prefix[idx]) % 26
            result += chr(ord('a') + temp)

        return result
        
