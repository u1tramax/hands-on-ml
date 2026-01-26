class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        cnt = 0
        for j in range(len(nums)):
            i = len(nums) - 1
            while i > 0:
                if nums[i-1] > nums[i]:
                    nums[i-1] = nums[i-1] + nums[i]
                    del nums[i]
                    cnt += 1
                i -= 1
        return cnt
        
nums = [5,2,3,1]
print(Solution().minimumPairRemoval(nums))