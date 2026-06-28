class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        brackets = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in brackets:
                if not q or q.pop() != brackets[char]:
                    return False
            else:
                q.append(char)
        return not q 
        