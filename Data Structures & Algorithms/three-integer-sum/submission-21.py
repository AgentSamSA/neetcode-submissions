class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                target = nums[j] + nums[k]
                if -nums[i] == target:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
                elif -nums[i] > target:
                    j += 1
                else:
                    k -= 1
        
        return output