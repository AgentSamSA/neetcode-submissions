class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        max_freq = 0
        left = 0
        longest = 0

        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            max_freq = max(max_freq, freqs[s[right]])

            while (right - left + 1) - max_freq > k:
                freqs[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest