class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            n = len(s)
            encoded += str(n)+"分"+s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        n = ""
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                n += s[i]
                i+=1
            if s[i] == "分":
                length = int(n)
                n = ""
                if length == 0:
                    res.append("")
                    i+=1
                else:
                    res.append(s[i+1:i+length+1])
                    i += length +1
        return res


        
