# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # BFS
        # res = 0

        # q = deque([root])

        # while q:
        #     node =q.popleft()
        #     res += 1

        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        # return res        

        # DFS
        res = 0
        stack = [root]

        while stack:
            node = stack.pop()
            res += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res