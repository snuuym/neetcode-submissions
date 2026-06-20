class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            if s2[i] in s1:
                sub_string = s2[i:i+len(s1)]
                if Counter(sub_string) == Counter(s1):
                    return True
        return False
        