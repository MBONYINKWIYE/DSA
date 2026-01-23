class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        target = Counter(s1)

        for _ in range(len(s2)):
            perm = Counter(s2[left:right])

            if perm == target:
                return True
            right += 1
            left +=1
        return False