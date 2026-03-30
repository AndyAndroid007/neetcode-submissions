class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = 0
        maxL = 0
        for j in range(len(s)):
            if s[j] in d and d[s[j]] >= i:
                i = d[s[j]]+1
            d[s[j]] = j
            maxL = max(maxL, j-i+1)
        return maxL