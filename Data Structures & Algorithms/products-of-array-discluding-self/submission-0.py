class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = [1]
        n = len(nums)
        right = [1]
        for i in range(n-1):
            curr = nums[i]*left[-1]
            left.append(curr)
        for j in range(n-1, 0, -1):
            curr = nums[j]*right[-1]
            right.append(curr)
        
        for i in range(n):
            product = left[i]*right[n-i-1]
            res.append(product)
        return res
        

            
        