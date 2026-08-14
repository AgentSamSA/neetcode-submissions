from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_elements = []

        q = deque()

        left = 0
        for right in range(len(nums)):

            if right - left + 1 > k:
                left += 1
            
            while q and q[-1][0] < nums[right]:
                q.pop()
            
            q.append((nums[right], right))

            while q and q[0][1] < left:
                q.popleft()
            
            if right - left + 1 == k:
                max_elements.append(q[0][0])
        
        return max_elements