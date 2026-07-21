class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        pre_product = 1
        for i in range(len(nums)):
            prefix.append(pre_product)
            pre_product *= nums[i]
        
        print(prefix)
        
        suf_product = 1
        for j in range(len(nums) - 1, -1, -1):
            suffix.append(suf_product)
            suf_product *= nums[j]

        print(suffix)

        for i in range(len(prefix)):
            prefix[i] *= suffix[len(suffix) - i - 1]

        return prefix