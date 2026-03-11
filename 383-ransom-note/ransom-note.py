class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)

        for m in magazine:
            count[m] += 1
        
        for r in ransomNote:
            if r not in count or count[r] == 0:
                return False
            count[r] -= 1
        return True


        