1class Solution:
2    def productExceptSelf(self, nums):
3        n = len(nums)
4        result = [1] * n
5        
6        prefix = 1
7        for i in range(n):
8            result[i] = prefix
9            prefix *= nums[i]
10        
11        suffix = 1
12        for i in range(n - 1, -1, -1):
13            result[i] *= suffix
14            suffix *= nums[i]
15        
16        return result