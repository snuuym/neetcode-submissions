class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n-1
        maxi = 0
        while i < j:
            water = min(heights[i], heights[j])*(j-i)
            maxi = max(water, maxi)
            if heights[i]>heights[j]:
                j -= 1
            else:
                i += 1
        return maxi            
            

        