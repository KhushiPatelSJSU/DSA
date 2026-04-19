class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ctRansom = {}
        ctMagazine = {}

        for x in ransomNote:
            if x in ctRansom:
                ctRansom[x] += 1
            else:
                ctRansom[x] = 1

        for x in magazine:
            if x in ctMagazine:
                ctMagazine[x] += 1
            else:
                ctMagazine[x] = 1

        for ch in ctRansom:
            if ch not in ctMagazine or ctMagazine[ch] < ctRansom[ch]:
                return False
        
        return True