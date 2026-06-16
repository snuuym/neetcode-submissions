class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        length = 0
        for num in nums:
            if num-1 not in nums:
                streak = 1
                while num + streak in nums:
                    streak +=1
                length = max(length, streak)
        return length

