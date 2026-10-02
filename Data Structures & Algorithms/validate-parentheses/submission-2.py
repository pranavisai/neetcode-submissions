class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if len(s) < 2:
            return False
        for i in s:
            if i == "{" or i == "(" or i == "[":
                st.append(i)
            else:
                if st and (
                (st[-1] == "(" and i == ")") or
                (st[-1] == "{" and i == "}") or
                (st[-1] == "[" and i == "]")):
                    st.pop()
                else:
                    return False
        return not st


        