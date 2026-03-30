class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = Counter(s1)
        d2 = Counter()
        left = 0
        
        for right in range(len(s2)):
            d2[s2[right]] = d2.get(s2[right],0) + 1
            if ((right - left + 1) > len(s1)):
                d2[s2[left]]-=1
                left+=1
            if right - left + 1 == len(s1):
                if d1 == d2:
                    return True
        return False



        