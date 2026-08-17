class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        freqs_t = {}
        freqs_s = {}
        substring = ''
        substring_len = float('inf')

        for char in t:
            freqs_t[char] = freqs_t.get(char, 0) + 1
        
        left = 0
        satisfied = 0
        for right in range(len(s)):
            if s[right] in freqs_t:
                freqs_s[s[right]] = freqs_s.get(s[right], 0) + 1
                if freqs_s[s[right]] == freqs_t[s[right]]:
                    satisfied += 1
            
            while satisfied == len(freqs_t):
                if right - left + 1 < substring_len:
                    substring = s[left:right + 1]
                    substring_len = right - left + 1
                if s[left] in freqs_t:
                    freqs_s[s[left]] -= 1
                    if freqs_s[s[left]] < freqs_t[s[left]]:
                        satisfied -= 1
                left += 1
        
        return substring