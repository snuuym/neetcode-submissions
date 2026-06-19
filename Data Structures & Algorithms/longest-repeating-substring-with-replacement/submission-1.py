class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #only for the current window
        l = 0 #left index
        maxf = 0 #maximum frequency
        res = 0
        for r in range(len(s)): #loop through the right index
            count[s[r]] = 1+ count.get(s[r],0) #if not found return 0
            maxf = max(maxf, count[s[r]]) 
            while r-l+1-maxf > k:  #when all the change chances are used
                count[s[l]] -=1 #count the current window 
                l += 1 #shrink the sliding window
            res = max(res, r-l+1)
        return res
                    





        