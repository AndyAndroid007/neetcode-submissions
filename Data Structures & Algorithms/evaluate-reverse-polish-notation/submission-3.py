class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evalu(a,b,o):
            if o == '+':
                return a+b
            elif o == '-':
                return b-a
            elif o == '*':
                return a*b
            elif o == '/':
                return int(b/a)
        s = []
        for i in tokens:
            if s and i in ('+','-','*','/'):
                a = s.pop()
                b = s.pop()
                x = evalu(a,b,i)
                s.append(x)
            else:
                s.append(int(i))
        if s:
            return s[0]