1class Solution:
2    def plusOne(self, digits: list[int]) -> list[int]:
3        for i in range(len(digits) - 1, -1, -1):
4            if digits[i] < 9:
5                digits[i] += 1
6                return digits
7            digits[i] = 0
8
9        return [1] + digits