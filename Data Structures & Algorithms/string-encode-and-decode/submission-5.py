class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            str_len = len(s)
            encoded += f'{str_len}#{s}'
        
        print('encoded str:', encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        num = ""
        i = 0
        while i < len(s):
            print('num before decimal check:', num)
            if s[i].isdecimal():
                num += s[i]
                i += 1
                print('num, i after decimal check:', num, i)
            
            if s[i] == '#' and s[i - 1].isdecimal():
                print('num at # check:', num)
                num = int(num)
                start = i + 1
                print('start:', start)
                end = num + start
                print('end:', end)

                decoded.append(s[start:end])
                
                i = end
                num = ""

        return decoded            