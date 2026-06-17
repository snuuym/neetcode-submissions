class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums)-2:
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j]+ nums[k] == -nums[i]:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[j]+ nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return res

            
        