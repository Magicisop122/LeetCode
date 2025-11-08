class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Functional recursion

        # newS = ''.join(c.lower() for c in s if c.isalnum())

        # def valid(i):
        #     if i >= (len(newS) // 2):

        #         return True
            
        #     if newS[i] != newS[len(newS) - i - 1]:
        #         return False
            
        #     return valid(i + 1)

        # return valid(0)



        #  regex method

        # s = s.lower()

        # c = re.sub(r'[^a-z0-9]', '', s)

        # return c == c[::-1]

        # 2 Pointers

        newS = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(newS) - 1

        while l <= r:
            if newS[l] != newS[r]:
                return False
            
            l += 1
            r -= 1
        
        return True