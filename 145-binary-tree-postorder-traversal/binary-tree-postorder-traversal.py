# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        # stack(iterative solution)

        stack = [root]
        visited = [False]
        res = []

        while stack:
            curr, v = stack.pop(), visited.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
            
        return res

        
        