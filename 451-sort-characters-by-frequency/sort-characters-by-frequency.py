class Solution:
    def frequencySort(self, s: str) -> str:

        mapS = {}

        for char in s:
            mapS[char] = mapS.get(char, 0) + 1

        sorted_chars = sorted(mapS.items(), key = lambda x: x[1], reverse = True)

        res = ""

        for i, e in sorted_chars:
            res += i * e

        return res
