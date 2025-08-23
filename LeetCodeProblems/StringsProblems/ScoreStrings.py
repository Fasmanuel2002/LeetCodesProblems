class Solution(object):
    def scoreOfString(self, s):
        operation = 0
        for letter in range(len(s) - 1):
            operation += abs(ord(s[letter]) - ord(s[letter + 1]))
        return operation