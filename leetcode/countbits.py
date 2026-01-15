class Solution:
    def countBits(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        power = 2
        result = [0, 1]
        while len(result) <= n:
            for i in range(0, power):
                result.append(result[i] + 1)
                if len(result) > n:
                    break
            power <<= 1
        return result[:n+1]
    
print(Solution().countBits(2))  

# 0 0
# 1 1
# 10 1
# 11 2
# 100 1 + 0 = 1
# 101 1 + 1 = 2
# 110 1 + 1 = 2
# 111 1 + 2 - 3
# 1000
