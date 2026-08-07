class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        total_area = 0

        while left < right:
            if left_max < right_max:
                area = left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                area = right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])

            total_area += area
        
        return total_area