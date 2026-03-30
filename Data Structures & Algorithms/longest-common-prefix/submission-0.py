class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = float('inf')
        for i in strs:
            minLen = min(minLen, len(i))
        j = 0
        ans = ""
        while j < minLen:
            check = strs[0][j]
            for k in strs:
                if k[j] != check:
                    return ans
            ans += check
            j+=1
        return ans
                        