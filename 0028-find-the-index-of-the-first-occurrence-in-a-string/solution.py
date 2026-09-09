class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = len(needle)

        for left in range(len(haystack) - k + 1):
            if haystack[left:left + k] == needle:
                return left

        return -1
        
