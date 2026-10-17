class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        st = []
        for i in operations:
            print(st)
            if i == "+":
                j = st[-1]
                k = st[-2]
                st.append(j+k)
            elif i == "D":
                j = st[-1]
                st.append(j * 2)
            elif i == "C":
                st.pop()
            else:
                j = int(i)
                st.append(j)
        return sum(st)
        