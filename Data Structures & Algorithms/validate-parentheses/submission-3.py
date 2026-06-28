class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        opens = ["(","{","["]
        closes = [")","]","}"]
        for char in s:
            if char in opens:
                q.append(char)
            else:
                if not q:
                    return False
                last = q.pop()
                if (last == "(" and char == ")") or (last == "[" and char == "]") or (last == "{" and char == "}"):
                    continue
                else:
                    return False
        return not q or False
        