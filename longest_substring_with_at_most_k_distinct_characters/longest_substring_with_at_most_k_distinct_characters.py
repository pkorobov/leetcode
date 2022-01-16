from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        window_counter = Counter()
        result = 0

        l = 0
        for r in range(len(s)):
            window_counter[s[r]] += 1

            while l < len(s) and len(window_counter) > k:
                window_counter[s[l]] -= 1
                if window_counter[s[l]] == 0:
                    del window_counter[s[l]]
                l += 1

            result = max(result, r - l + 1)
        return result