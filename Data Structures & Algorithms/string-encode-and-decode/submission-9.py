class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(f'{len(s)}#{s}')
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        num = ""
        i = 0
        while i < len(s):
            while s[i] != '#':
                num += s[i]
                i += 1
            
            length = int(num)
            i += 1
            decoded.append(s[i:i+length])
                
            i += length
            num = ""

        return decoded            