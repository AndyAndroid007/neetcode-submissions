class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sD = dict()
        tD = Counter(t)
        required = len(tD)
        minL = float('inf')
        minC = ""
        formed = 0
        i = j = 0
        while i <= j and j < len(s):
            curr = s[j]
            sD[curr] = sD.get(curr,0) + 1
            if curr in tD and sD[curr] == tD[curr]:
                formed += 1
            while formed == required:
                if j-i+1 < minL:
                    minL = j-i+1
                    minC = s[i:j+1]
                rem = s[i]
                sD[rem]-=1
                if rem in tD and sD[rem] < tD[rem]:
                    formed-=1
                i+=1
            j+=1
        return minC

        