class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    nums_list = [i, j]
                    break
        
        return nums_list