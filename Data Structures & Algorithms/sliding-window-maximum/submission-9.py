from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        max_elements = []

        left = 0
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            if right - left + 1 > k:
                left += 1

            while q and q[0] < left:
                q.popleft()
            
            if q and right - left + 1 == k:
                max_elements.append(nums[q[0]])

        return max_elements