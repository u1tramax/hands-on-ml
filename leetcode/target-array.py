class Solution:
    def minOperations(self, nums: list[int], target: list[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != target[i]:
                curr = nums[i]
                for j in range(i, len(nums)):
                    if nums[j] == curr:
                        nums[j] = target[j]
                cnt += 1
        return cnt

nums = [7,3,7]
target = [5,5,9]
print(Solution().minOperations(nums, target))