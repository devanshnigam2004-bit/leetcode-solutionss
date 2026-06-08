1class Solution:
2    def titleToNumber(self, columnTitle: str) -> int:
3        result = 0
4
5        for char in columnTitle:
6            result = result * 26 + (ord(char) - ord('A') + 1)
7
8        return result