class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        bars = []
        for i in range(len(heights)+1):
            while bars and (i == len(heights) or heights[i] < bars[-1][0]):
                height, index = bars.pop()
                width = i if not bars else i-1-bars[-1][1]
                area = height*width
                max_area = max(max_area, area)
            if i != len(heights):
                bars.append([heights[i],i])
        
        return max_area


        