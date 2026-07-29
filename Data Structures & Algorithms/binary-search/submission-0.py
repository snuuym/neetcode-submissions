class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n
        while i<j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid
            else:
                i = mid+1
        return -1

        