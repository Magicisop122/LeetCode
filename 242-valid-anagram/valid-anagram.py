class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        hashmap = {}

        for n in s:
            hashmap[n] += 1

            
        