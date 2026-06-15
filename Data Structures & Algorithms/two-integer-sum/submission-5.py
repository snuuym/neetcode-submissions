class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted([[i,num] for i,num in enumerate(nums)], key = lambda x: x[1])
        i = 0
        j = len(nums)-1
        while i<j:
            if sorted_nums[i][1]+sorted_nums[j][1] == target:
                return sorted( [sorted_nums[i][0],sorted_nums[j][0]] )
            elif sorted_nums[i][1]+sorted_nums[j][1] > target:
                j -= 1
            else:
                i += 1
            



        