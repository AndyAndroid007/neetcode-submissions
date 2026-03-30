class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = Counter(t)
        d2 = Counter()
        formed = 0
        required = len(d1)
        minwin = ""
        left = 0
        for right in range(len(s)):
            if s[right] in d1:
                d2[s[right]] = d2.get(s[right],0)+1
                if d2[s[right]] == d1[s[right]]:
                    formed+=1

            
            while formed == required:
                if( minwin == "" or (right-left+1 < len(minwin))):
                    minwin = s[left:right+1]
                if s[left] in d1:
                    d2[s[left]]-=1
                    if d2[s[left]] < d1[s[left]]:
                        formed-=1
                    if d2[s[left]] == 0:
                        del d2[s[left]]
                left+=1
            print(d2)
        return minwin
        