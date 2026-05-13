class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j = 0,0
        for i in range(len(s)):
            if j == len(t):
                return 0
            if s[i] == t[j]:
                j+=1
        print(i,j)
        if j == len(t):
            return 0
        return len(t)-j

        