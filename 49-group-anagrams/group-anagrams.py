class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting solution

        anagrams = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())

        # hashmap solution

        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return list(result.values())
        