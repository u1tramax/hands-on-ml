from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node, visited_out):
            stack = [node]
            n = len(isConnected)

            while stack:
                curr = stack.pop()
                visited_out.add(curr)
                for i in range(n):
                    if isConnected[curr][i] == 1 and i not in visited_out:
                        stack.append(i)

        visited_out = set()
        cnt = 0
        for i, node in enumerate(isConnected):
            if i not in visited_out:
                cnt += 1
                dfs(i, visited_out)
        return cnt

                
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))