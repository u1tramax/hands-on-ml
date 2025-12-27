from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freqs = Counter(nums)
        pairs = 0
        for key, value in freqs.items(): 
            if key == k - key:
                pairs += value // 2
            elif key < k - key:
                pairs += min(value, freqs[k-key])
        return pairs
    
nums = [1, 2, 3, 4]
k = 5
print(Solution().maxOperations(nums, k))