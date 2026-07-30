class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []

        product = 1
        for num in nums:
            prefix.append(product)
            product *= num
        
        product = 1
        for i in range(len(prefix) - 1, -1, -1):
            prefix[i] *= product
            product *= nums[i]
        
        return prefix