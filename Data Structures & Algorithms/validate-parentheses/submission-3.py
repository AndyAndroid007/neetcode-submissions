class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        opens = set()
        opens.add('(')
        opens.add('{')
        opens.add('[')
        d = {'}':'{',']':'[',')':'('}
        for i in s:
            if i in opens:
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:

                if stack and stack.pop() != d[i]:
                    return False
        return len(stack) == 0
            
        