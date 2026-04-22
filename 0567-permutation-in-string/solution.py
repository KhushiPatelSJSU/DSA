class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}

        for x in s1:
            count1[x] = count1.get(x, 0) + 1

        left = 0

        for right in range(len(s2)):
            count2[s2[right]] = count2.get(s2[right], 0) + 1

            # shrink if window is bigger than length of shorter string 
            if right - left + 1 > len(s1):
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1

            if count1 == count2:
                return True

        return False
