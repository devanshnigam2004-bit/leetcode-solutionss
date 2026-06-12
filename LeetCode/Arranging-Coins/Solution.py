1class Solution:
2    def arrangeCoins(self, n: int) -> int:
3        low, high = 1, n
4
5        while low <= high:
6            mid = (low + high) // 2
7            coins = mid * (mid + 1) // 2
8
9            if coins == n:
10                return mid
11            elif coins < n:
12                low = mid + 1
13            else:
14                high = mid - 1
15
16        return high