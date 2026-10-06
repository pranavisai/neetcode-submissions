class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i not in "+-*/":
                s.append(int(i))
            else:
                if s:
                    t = s.pop()
                    n = s.pop()
                    if i == "+":
                        s.append(t + n)
                    elif i == "-":
                        s.append(n - t)
                    elif i == "*":
                        s.append(t*n)
                    else:
                        s.append(int(n / t))
        return s[-1]
                        
        