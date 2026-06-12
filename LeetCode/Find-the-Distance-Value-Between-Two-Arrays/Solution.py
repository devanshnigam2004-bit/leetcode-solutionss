1class Solution:
2    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
3        arr2.sort()
4        count = 0
5
6        for num in arr1:
7            if self.isValid(arr2, num, d):
8                count += 1
9
10        return count
11
12    def isValid(self, arr2, num, d):
13        low, high = 0, len(arr2) - 1
14
15        while low <= high:
16            mid = (low + high) // 2
17
18            if abs(arr2[mid] - num) <= d:
19                return False
20            elif arr2[mid] < num:
21                low = mid + 1
22            else:
23                high = mid - 1
24
25        return True