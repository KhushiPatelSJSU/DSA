class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mapS = {}
        mapT = {}

        for i in s:
            mapS[i] = mapS.get(i, 0) + 1
        
        for i in t:
            mapT[i] = mapT.get(i, 0) + 1

        for i in mapT:
            if i not in mapS or mapT[i] != mapS[i]:
                return i
