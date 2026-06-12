1class Solution:
2    def missingNumber(self, nums: list[int]) -> int:
3        n = len(nums)
4        expected = n * (n + 1) // 2
5        return expected - sum(nums)