1class Solution:
2    def maxSubArray(self, nums: list[int]) -> int:
3        left = 0
4        current = 0
5        max_sum = float('-inf')
6
7        for right in range(len(nums)):
8            current += nums[right]
9            max_sum = max(max_sum, current)
10
11            if current < 0:
12                current = 0
13                left = right + 1
14
15        return max_sum