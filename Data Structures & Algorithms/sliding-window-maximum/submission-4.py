import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements = []

        max_heap = []
        heapq.heapify(max_heap)
    
        left = 0
        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))

            if right - left + 1 > k:
                left += 1
            
            if right - left + 1 == k:
                curr = max_heap[0]
                while curr[1] < left:
                    heapq.heappop(max_heap)
                    curr = max_heap[0]
                max_elements.append(-curr[0])
        
        return max_elements