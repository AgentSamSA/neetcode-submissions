class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        max_freq = 0
        longest = 0
        left = 0
        right = 0
        
        while right < len(s):

            freqs[s[right]] = freqs.get(s[right], 0) + 1
            max_freq = max(max_freq, freqs[s[right]])
            
            while left < right and (right - left + 1) - max_freq > k:
                freqs[s[left]] = freqs.get(s[left], 0) - 1
                left += 1
            
            longest = max(longest, right - left + 1)
            right += 1
        
        return longest