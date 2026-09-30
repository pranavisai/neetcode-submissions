class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1
        while(i < j):
            k = heights[i]
            m = heights[j]
            if k < m:
                p = k * (j-i)
                i += 1
            else:
                p = m * (j-i)
                j -= 1
            area = max(area,p)
        return area


        