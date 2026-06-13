1class Solution:
2    def integerReplacement(self, n: int) -> int:
3        count = 0
4
5        while n != 1:
6            if n % 2 == 0:
7                n >>= 1
8            elif n == 3 or ((n >> 1) & 1) == 0:
9                n -= 1
10            else:
11                n += 1
12            count += 1
13
14        return count