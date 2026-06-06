1class Solution:
2    def maximumProduct(self, nums: list[int]) -> int:
3        nums.sort()
4        n = len(nums)
5        return max(nums[n-1] * nums[n-2] * nums[n-3],
6                   nums[0] * nums[1] * nums[n-1])