"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return None

        old_to_new = {}

        def dfs(old_node):
            if old_node in old_to_new:
                return old_to_new[old_node]

            new_node = Node(old_node.val)
            old_to_new[old_node] = new_node

            for neighbor in old_node.neighbors:
                new_neighbor = dfs(neighbor)
                new_node.neighbors.append(new_neighbor)

            return new_node

        return dfs(node)

## Jun 16, 2026 -> 이해를 하긴..? 했지만 (겨우) 엄청 어려웠음 !
## 문제 자체가 이해가 되지 않았으며, ai를 통해 그 흐름을 익히고 난 후에도 그 직관적 코드의 흐름이
## 머리속에서 또렷하게 그려지지 않음 
## 훗날 다시 Node에 대해 익숙해진 뒤, 혼자 재 작성 해볼 수 있도록 ! 

# 엥 