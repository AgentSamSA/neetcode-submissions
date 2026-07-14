class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in candidates:
                candidates[num].append(i)
            else:
                candidates[num] = [i]
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in candidates:
                if len(candidates[diff]) > 1:
                    return candidates[diff]
                elif candidates[diff][0] != i:
                    return [candidates[nums[i]][0], candidates[diff][0]]
