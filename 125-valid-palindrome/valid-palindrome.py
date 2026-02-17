class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cheating solution because it uses python in built functions

        newString = ""

        for c in s:
            if c.isalnum():
                newString += c.lower()
        return newString == newString[::-1]