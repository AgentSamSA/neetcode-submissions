class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = [0] * 26
        left = 0
        right = len(s1) - 1

        for char in s1:
            index = ord(char) - ord('a')
            freq_s1[index] += 1
        
        freq_window = [0] * 26
        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            freq_window[index] += 1

        while right < len(s2):

            if freq_window == freq_s1:
                return True
            elif right + 1 == len(s2):
                return False
            
            left_index = ord(s2[left]) - ord('a')
            freq_window[left_index] -= 1
            left += 1
            right += 1
            right_index = ord(s2[right]) - ord('a')
            freq_window[right_index] += 1
        
        return False
