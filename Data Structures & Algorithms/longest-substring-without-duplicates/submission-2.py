class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        maxlen = 0
        d = {}
        while j < len(s):
            if s[j] in d and d[s[j]] >= i:
                i = d[s[j]] + 1
            d[s[j]] = j
            maxlen = max(maxlen, j - i + 1)
            j += 1
        return maxlen
