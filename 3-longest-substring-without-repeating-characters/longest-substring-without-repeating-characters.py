class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # charSet = set()
        # res = 0
        # l = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)

        # return res

        # brute force

        if len(s) == 0:
            return 0
        result = 1

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):
                if s[j] in seen:
                    result = max(result, j - i)
                    break
                seen.add(s[j])
                result = max(result, len(seen))
                

        return result

        
        