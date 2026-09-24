class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = []
        for i in range(0, len(arr)-1):
            j = max(arr[i+1:])
            a.append(j)
        a.append(-1)
        return a


        