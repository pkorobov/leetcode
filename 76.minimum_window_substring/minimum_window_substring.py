from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        ct = Counter(t)
        window_counts = Counter()
        count = 0
        ansl, ansr = -1, len(s)

        i = 0
        for j in range(len(s)):
            if s[j] in ct:
                window_counts[s[j]] += 1
                if window_counts[s[j]] <= ct[s[j]]:
                    count += 1
            else:
                continue
            if count < len(t):
                continue

            while i < len(s) and count == len(t):
                if s[i] in ct:
                    window_counts[s[i]] -= 1
                    if window_counts[s[i]] < ct[s[i]]:
                        count -= 1
                    if count < len(t):
                        if ansr - ansl > j - i:
                            ansl, ansr = i, j + 1
                i += 1
        if ansl == -1:
            return ""
        return s[ansl:ansr]
