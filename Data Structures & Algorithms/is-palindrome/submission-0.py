class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join([char for char in s if char.isalnum()]).lower()

        print(clean)
        for i in range(len(clean) // 2):
            print('curr', clean[i])
            print('end', clean[-i])
            print('i', i)
            if clean[i] != clean[-(i+1)]:
                return False

        return True