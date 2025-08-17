class Solution:
    def maxDepth(self, s: str) -> int:

        res = 0
        cnt = 0

        for ch in s:
            
            if ch == '(':
                cnt += 1
            elif ch == ')':
                cnt -= 1
            res = max(res, cnt)

        return res

                
        