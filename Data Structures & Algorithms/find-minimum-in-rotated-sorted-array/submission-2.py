class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        i = 0
        j = n-1
        while i<j:
            if nums[i]<nums[j]:
                return nums[i]
            else:
                i += 1
        return nums[j]
        

        