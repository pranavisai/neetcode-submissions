class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stk = []

        for i, temp in enumerate(temperatures):
            while stk and stk[-1][1] < temp:
                j, t = stk.pop()
                ans[j] = i - j
            stk.append((i,temp))
        return ans


        