# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    values: список в level-order, None = отсутствующий узел
    Пример: [1, 2, 3, None, 4]
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        stack = [(root, {})]
        while stack:
            
            node, sums = stack.pop()

            sums[node.val] = sums.get(node.val, 0)

            sums.append(node.val)
            if node.val == targetSum:
                cnt += 1

            if node.left:
                stack.append((node.left, sums.copy()))
            if node.right:
                stack.append((node.right, sums.copy()))

        return cnt
    
root = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
targetSum = 8
print(Solution().pathSum(root, targetSum))