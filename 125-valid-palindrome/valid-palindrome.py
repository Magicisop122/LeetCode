class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cheating solution because it uses python in built functions

        # newString = ""

        # for c in s:
        #     if c.isalnum():
        #         newString += c.lower()
        # return newString == newString[::-1]

        # optimal way of solving using 2 pointers

        def isAlnum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))

        l, r = 0, len(s) - 1


        while l < r:
            while l < r and not isAlnum(s[l]):
                l += 1
            while r > l and not isAlnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
        
            l += 1
            r -= 1
        
        return True
            



        