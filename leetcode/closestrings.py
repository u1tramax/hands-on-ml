from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        chars1 = Counter(word1).values()
        chars2 = Counter(word2).values()
        print(chars1, chars2)
        if sorted(chars1) == sorted(chars2):
            return True
        return False
    
word1 = "cabbba"
word2 = "abbccc"

print(Solution().closeStrings(word1, word2))