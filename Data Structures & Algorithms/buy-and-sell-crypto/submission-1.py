class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        sort = [prices[0]]
        heapq.heapify(sort)
        for i in range(1, len(prices)):
            heapq.heappush(sort,prices[i])
            res = max(res, prices[i]-sort[0])
            
        return res

        