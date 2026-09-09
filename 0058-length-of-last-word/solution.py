class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the string to trim extra spaces and get the words only.
        # Then get the length of last word from the list
        return len(s.split()[-1])
