class Solution:
    def isPalindrome(self, s: str) -> bool:

        newS = ''.join(c.lower() for c in s if c.isalnum())

        def valid(i):
            if i >= (len(newS) // 2):

                return True
            
            if newS[i] != newS[len(newS) - i - 1]:
                return False
            
            return valid(i + 1)

        return valid(0)



        #  regex method

        # s = s.lower()

        # c = re.sub(r'[^a-z0-9]', '', s)

        # return c == c[::-1]

        