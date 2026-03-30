class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = []
        def backtrack(o,c,s):
            if o == n and c == n:
                s1 = s
                final.append(s1)
            if o < n:
                backtrack(o+1,c,s+'(')
            if c < o:
                backtrack(o,c+1,s+')')
        backtrack(0,0,"")
        return final
        

        