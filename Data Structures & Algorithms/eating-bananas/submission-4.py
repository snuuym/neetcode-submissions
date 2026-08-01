class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        most = max(piles)
        i = 1
        j = most
        while i<j:
            mid = (i+j)//2
            time = 0
            for num in piles:
                time+= math.ceil(num / mid)
            if time>h:
                i = mid+1
            else:
                j = mid
        return j

        