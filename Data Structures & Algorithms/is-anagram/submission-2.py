class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = Counter(s)
        d2 = Counter(t)
        if d1 == d2:
            return True
        return False
        for i in d1:
            if i not in d2:
                return False
            else:
                if d1[i] != d2[i]:
                    return False
        return True

        