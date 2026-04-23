1class Solution:
2    def findGCD(self, nums):
3        def gcd(a, b):
4            while b:
5                a, b = b, a % b
6            return a
7        
8        return gcd(min(nums), max(nums))