class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n
        pos = 1
        pref = 1
        for i in range(n):
            res[i] *= pos
            pos *= nums[i]
        for j in range(n-1, -1, -1):
            res[j] *= pref
            pref *= nums[j]
        return res
        

            
        