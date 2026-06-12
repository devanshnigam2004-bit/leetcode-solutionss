1class Solution:
2    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
3        low, high = 0, len(letters) - 1
4        result = letters[0]
5
6        while low <= high:
7            mid = (low + high) // 2
8
9            if letters[mid] > target:
10                result = letters[mid]
11                high = mid - 1
12            else:
13                low = mid + 1
14
15        return result