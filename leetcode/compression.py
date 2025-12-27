from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        result = ''
        cur_char = ''#chars[0]
        cnt = 0
        for i, char in enumerate(chars):
            if cur_char == char:
                cnt += 1
                if i == len(chars) - 1:
                    result += cur_char
                    if cnt > 1:
                        result += str(cnt)
            else:
                result += cur_char
                if cnt > 1:
                    result += str(cnt)
                cnt = 1
                cur_char = char
        
        return result
    
chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))