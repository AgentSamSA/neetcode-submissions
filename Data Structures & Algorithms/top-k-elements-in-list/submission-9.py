class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freqs.items():
            buckets[freq].append(num)
        
        most_frequent = []
        for bucket in buckets:
            for num in bucket:
                most_frequent.append(num)
        
        return most_frequent[-k:]