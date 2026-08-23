from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        maximums = []

        left = 0
        for right in range(len(nums)):
            if right - left + 1 > k:
                left += 1

            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            while q and q[0] < left:
                q.popleft()
            
            if right - left + 1 == k:
                maximums.append(nums[q[0]])              
        
        return maximums