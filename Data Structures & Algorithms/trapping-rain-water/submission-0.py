class Solution:
    def trap(self, height: List[int]) -> int:
        #to trap water, taller on both side. 2 pointer?
        n = len(height)
        #vol = (min(left_height,right_height)-cur_height)*width(1)
        left_highest = height[0]
        lefts = []
        rights = [0]*n
        right_highest = height[n-1]
        for i in range(n):
            left_highest = max(left_highest, height[i])
            right_highest = max(right_highest,height[n-1-i])
            lefts.append(left_highest)
            rights[n-1-i]=right_highest
        res = 0
        for i in range(n):
            area = min(lefts[i],rights[i])-height[i]
            res += area
        return res

        
