class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqs_s1 = [0] * 26
        left = 0

        for char in s1:
            freqs_s1[ord(char) - ord('a')] += 1
        
        freqs_window = [0] * 26
        for right in range(len(s2)):
            freqs_window[ord(s2[right]) - ord('a')] += 1
            
            if right - left + 1 > len(s1):
                freqs_window[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if right - left + 1 == len(s1):
                if freqs_window == freqs_s1:
                    return True
        return False
