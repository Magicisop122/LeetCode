class Solution:
    def isPalindrome(self, s: str) -> bool:

        # def valid(l: int, r: int) -> bool:
        #     if l >= r:
        #         return True

        #     while l < r and not s[l].isalnum():
        #         l += 1
            
        #     while l < r and not s[r].isalnum():
        #         r -= 1

        #     if l >= r:
        #         return True

        #     if s[l].lower() != s[r].lower():
        #         return False
            
        #     return valid(l + 1, r - 1)

        # return valid(0, len(s) - 1)


        #  regex method

        s = s.lower()

        c = re.sub(r'[^a-z0-9]', '', s)

        return c == c[::-1]