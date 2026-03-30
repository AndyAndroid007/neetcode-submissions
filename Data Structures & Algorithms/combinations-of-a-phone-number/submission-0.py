class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits) == 0:
            return []
        def backtrack(level, s):
            if len(s) == len(digits):
                s1 = s
                final.append(s)
                return
            
            for i in d[digits[level]]:
                backtrack(level+1, s + i)
        final = []
        backtrack(0, "")
        return final

        