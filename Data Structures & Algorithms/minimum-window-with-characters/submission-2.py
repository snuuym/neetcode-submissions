class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        if len(t) > len(s):
            return res
        counter_t = Counter(t)
        counter_s = {}
        l = 0
        have = 0
        need = len(counter_t)
        res_len = float("inf")
        curr = [-1,-1]
        for r in range(len(s)):
            counter_s[s[r]] = 1+counter_s.get(s[r],0)

            if counter_s[s[r]] == counter_t[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < res_len:
                    res_len = r-l+1
                    curr = [l,r]
                counter_s[s[l]] -= 1

                if s[l] in counter_t and counter_s[s[l]] < counter_t[s[l]]:
                    have -= 1
                l+=1
        l, r = curr
        return s[l:r+1] if res_len != float("inf") else ""

             





        