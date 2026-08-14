class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        freqs_t = {}
        freqs_window = {}
        shortest = ''
        shortest_len = float('inf')
        
        for char in t:
            freqs_t[char] = freqs_t.get(char, 0) + 1
        
        left = 0
        satisfied = 0
        for right in range(len(s)):
            char = s[right]
            if char in freqs_t:
                freqs_window[char] = freqs_window.get(char, 0) + 1
                if freqs_window[char] == freqs_t[char]:
                    satisfied += 1

            while satisfied == len(freqs_t):
                if right - left + 1 < shortest_len:
                    shortest = s[left:right + 1]
                    shortest_len = right - left + 1
                if s[left] in freqs_t:
                    freqs_window[s[left]] -= 1
                    if freqs_window[s[left]] < freqs_t[s[left]]:
                        satisfied -= 1
                left += 1
        
        return shortest