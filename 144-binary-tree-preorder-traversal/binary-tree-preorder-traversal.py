# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # recursion

        # if not root:
        #     return []
        # res = []
        
        # def dfs(root):
        #     if not root:
        #         return
        #     res.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        
        # return res


        # iterative
        if not root:
            return []

            
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)

            if curr.right:
                stack.append(curr.right)
            
            if curr.left:
                stack.append(curr.left)

        return res

        
        