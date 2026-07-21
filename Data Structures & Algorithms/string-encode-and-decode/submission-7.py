class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            str_len = len(s)
            encoded += f'{str_len}#{s}'
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        num = ""
        i = 0
        while i < len(s):
            if s[i].isdecimal():
                num += s[i]
                i += 1
            
            if s[i] == '#' and s[i - 1].isdecimal():
                num = int(num)
                start = i + 1
                end = num + start

                decoded.append(s[start:end])
                
                i = end
                num = ""

        return decoded            