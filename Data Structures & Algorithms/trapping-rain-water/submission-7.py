class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        length = len(height)
        pre_max = [0] * length
        suf_max = [0] * length
        pre_max[0], suf_max[length - 1] = height[0], height[length - 1]

        for i in range(1, length):
            pre_max[i] = max(pre_max[i - 1], height[i])
        
        for i in range(length - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        #print(pre_max)
        #print(suf_max)

        for i in range(length):
            max_left = pre_max[i]
            max_right = suf_max[i]

            area = min(max_left, max_right) - height[i]
            total_area += area
        
        return total_area