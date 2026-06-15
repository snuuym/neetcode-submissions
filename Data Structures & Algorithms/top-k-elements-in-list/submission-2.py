class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        if len(counts) == 1:
            return [nums[0]]

        res = []
        for num, count in counts.items():
                heapq.heappush(res, (count, num))
                if len(res) > k:
                    heapq.heappop(res)
        return [item[1]for item in res]
        

    
