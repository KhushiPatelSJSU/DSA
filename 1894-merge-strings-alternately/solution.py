class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1), len(word2)
        i = 0
        merged = ''

        while i < n and i < m:
            merged += word1[i] + word2[i]
            i += 1

        if i < n:
            merged += word1[i:]
        else:
            merged += word2[i:]

        return merged
