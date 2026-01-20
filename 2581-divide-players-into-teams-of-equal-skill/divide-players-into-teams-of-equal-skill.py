class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left = 0
        right =len(skill)-1
        skill.sort()
        product = 0
        while left < right:
            if skill[left] + skill[right] == skill[left + 1] + skill[right -1]:
                product += skill[left] * skill[right]
                left += 1
                right -= 1
            else:
                return -1
        return product