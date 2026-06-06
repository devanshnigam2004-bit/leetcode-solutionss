1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x < 2:
4            return x
5
6        low, high = 1, x // 2
7
8        while low <= high:
9            mid = (low + high) // 2
10
11            if mid * mid == x:
12                return mid
13            elif mid * mid < x:
14                low = mid + 1
15            else:
16                high = mid - 1
17
18        return high