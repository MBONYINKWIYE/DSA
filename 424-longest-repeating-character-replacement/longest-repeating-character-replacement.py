class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, most_freq, result, freq = 0, 0, 0, 0, defaultdict(int)
        while right < len(s):
            freq[s[right]] += 1
            most_freq = max(most_freq, freq[s[right]])
            while (right - left +1) - most_freq > k:
                freq[s[left]] -= 1
                left += 1
            result = max(result, right - left +1)
            right += 1
        return result

