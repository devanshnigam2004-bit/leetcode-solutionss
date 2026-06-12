1class Solution:
2    def targetIndices(self, nums: list[int], target: int) -> list[int]:
3        nums.sort()
4        result = []
5
6        for i in range(len(nums)):
7            if nums[i] == target:
8                result.append(i)
9
10        return result