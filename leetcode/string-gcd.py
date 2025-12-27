class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        substring = str1 if len(str1) > len(str2) else str2
        while substring:
            if ''.join(str1.split(substring)) == '' and ''.join(str2.split(substring)) == '':
                return substring
            else:
                substring = substring[:-1]
        return ''
    
    def gcdOfStrings2(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ''
        
        import math
        substring_length =  math.gcd(len(str1), len(str2))
        return str1[:substring_length]

a = Solution()
str1, str2 = 'ABCABC', 'ABC'
print(a.gcdOfStrings2(str1, str2))