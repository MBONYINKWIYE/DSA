class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_point = 0
        highest_alt = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            curr_point += gain[i]
            highest_alt[i] = curr_point
            
        print(highest_alt)
        return max(highest_alt)
