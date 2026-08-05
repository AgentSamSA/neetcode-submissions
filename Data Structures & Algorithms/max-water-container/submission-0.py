class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # set two pointers
        # create a box and compare that area with the max we have set
        # if our new area is bigger than max, set it to max
        # if left side is smaller, increment, otherwise increment right
        max = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if area > max:
                max = area
            if left < right and heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max