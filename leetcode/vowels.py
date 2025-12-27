class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cur = 0
        vowels = set(list('aeiou'))
        for i in range(k):
            if s[i] in vowels:
                cur += 1
        max_vowels = cur
        for i in range(len(s) - k):
            #cur = s[i:i+k]
            if s[i+k] in vowels:
                cur += 1
            if s[i] in vowels:
                cur -= 1
            if cur > max_vowels:
                max_vowels = cur
        return max_vowels
    
s = 'a'
k = 1
print(Solution().maxVowels(s, k))