class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1
        while(True):
            k = heights[i]
            m = heights[j]
            if i == j:
                break
            if k < m:
                p = k * (j-i)
                i += 1
            else:
                p = m * (j-i)
                j -= 1
            area = max(area,p)
        return area


        