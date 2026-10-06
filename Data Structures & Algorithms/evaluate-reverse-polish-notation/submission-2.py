class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        total = 0
        for i in tokens:
            if i not in "+-*/":
                s.append(int(i))
            else:
                if s:
                    t = s.pop()
                    n = s.pop()
                    if i == "+":
                        n = t + n
                    elif i == "-":
                        n = n - t
                    elif i == "*":
                        n = t*n
                    else:
                        n = int(n / t)
                    s.append(n)
        return s[-1]
                        
        