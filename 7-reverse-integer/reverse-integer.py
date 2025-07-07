class Solution:
    def reverse(self, x: int) -> int:

        revNum = 0
        isNegative = x < 0
        x = abs(x)

        while x != 0:
            lastDigit = x % 10
            revNum = (revNum * 10) + lastDigit
            x = x // 10

        if isNegative:
            revNum = -revNum

        if revNum < -2**31 or revNum > 2**31 - 1:
            return 0
        
        return revNum
        