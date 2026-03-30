class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        final = []
        for i in strs:
            x = ''.join(sorted(i))
            if x in d:
                d[x].append(i)
            else:
                d[x] = [i]
        
        for i in d.values():
            final.append(i)
        return final
        
        