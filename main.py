from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save = {}
        for i in range(len(nums)):
            if target - nums[i] in save:
                return [save[target - nums[i]], i]
            save[nums[i]] = i
        return [0, 1]

nums = [2,5,5,11]
target = 10
print(Solution().twoSum(nums, target))