from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1]
        right_products = [1]
        for num in nums:
            left_products.append(left_products[-1] * num)
        for num in nums[::-1]:
            right_products.append(right_products[-1] * num)
        print(left_products[1:], right_products[::-1])

nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))