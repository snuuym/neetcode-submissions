class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        sub = deque()
        longest = 1
        for char in s:
            if char not in sub:
                sub.append(char)
            else:
                longest = max(longest, len(sub))
                while sub[0] != char:
                    sub.popleft()
                sub.popleft()
                sub.append(char)
        longest = max(longest, len(sub))
        return longest


        