class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        left = 0
        right = 0

        while right < len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[right])
            longest = max(longest, right - left + 1)
            right += 1

        
        return longest