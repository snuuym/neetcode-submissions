class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        if len(nums) == 1:
            return [nums[0]]
        count = 1

        res = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                heapq.heappush(res, (count, nums[i-1]))
                if len(res) > k:
                    heapq.heappop(res)
                count = 1
        heapq.heappush(res,(count,nums[i]))
        if len(res)>k:
            heapq.heappop(res)
        return [item[1]for item in res]
        

    
