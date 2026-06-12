1class Solution:
2    def isPerfectSquare(self, num: int) -> bool:
3        if num < 2:
4            return True
5
6        low, high = 1, num // 2
7
8        while low <= high:
9            mid = (low + high) // 2
10
11            if mid * mid == num:
12                return True
13            elif mid * mid < num:
14                low = mid + 1
15            else:
16                high = mid - 1
17
18        return False