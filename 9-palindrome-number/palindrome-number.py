class Solution:
    def isPalindrome(self, x: int) -> bool:

        revNum = 0
        dup = x

        if x < 0:
            return False
        
        while x != 0:
            ld = x % 10
            revNum = (revNum * 10) + ld
            x = x // 10

        if revNum == dup:
            return True
        else: 
            return False
        