1class Solution:
2    def isHappy(self, n: int) -> bool:
3        def sumOfSquares(num):
4            total = 0
5            while num > 0:
6                digit = num % 10
7                total += digit * digit
8                num //= 10
9            return total
10
11        slow = n
12        fast = sumOfSquares(n)
13
14        while fast != 1 and slow != fast:
15            slow = sumOfSquares(slow)
16            fast = sumOfSquares(sumOfSquares(fast))
17
18        return fast == 1