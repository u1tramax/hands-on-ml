class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        ones, zeros = [], []
        ones_cnt, zeros_cnt = 0, 0

        for num in nums:
            if num == 1:
                ones_cnt += 1
                if zeros_cnt:
                    zeros.append(zeros_cnt)
                    zeros_cnt = 0
            elif num == 0:
                zeros_cnt += 1
                if ones_cnt:
                    ones.append(ones_cnt)
                    ones_cnt = 0

        if ones_cnt:
            ones.append(ones_cnt)
        if zeros_cnt:
            zeros.append(zeros_cnt)

        if not zeros:
            return ones[0] - 1
        
        print(ones, zeros)

        max_sum = 0
        for i in range(0, len(ones) - 1):
            max_sum = max(max_sum, ones[i] + ones[i+1])

        return max_sum

nums = [1,1,1]
print(Solution().longestSubarray(nums))
