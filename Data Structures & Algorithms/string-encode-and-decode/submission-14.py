class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(f'{len(s)}#{s}')
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []

        index = 0
        num = ''

        while index < len(s):
            
            while s[index] != '#':
                num += s[index]
                index += 1
            
            length = int(num)
            index += 1
            decoded.append(s[index:index + length])
            
            index += length
            num = ''
        
        return decoded
