class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence_starters = set(nums)
        longest = 0
        length = 0

        for num in nums:
            if num - 1 not in sequence_starters:
                length = 1
            else:
                continue
            
            curr = num
            while (curr + 1 in sequence_starters):
                curr += 1
                length += 1
            
            longest = max(longest, length)
        
        return longest