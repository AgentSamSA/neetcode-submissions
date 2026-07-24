class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(f'{len(s)}#{s}')
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        print(s)

        num = ''
        i = 0
        while i < len(s):
            while s[i].isdecimal():
                num += s[i]
                i += 1
                print('num', num)
                print('i', i)
            
            num = int(num)
            i += 1
            decoded.append(s[i:i+num])
            i += num
            num = ''
        
        return decoded