class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # track frequency of each element, order from largest to smallest, grab k values and return those keys.
        # map time?
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        sorted_freqs = sorted(freqs, key=freqs.get, reverse=True)

        return sorted_freqs[:k]