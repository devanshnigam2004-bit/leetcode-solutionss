1class Solution:
2    def majorityElement(self, nums: list[int]) -> int:
3        candidate = None
4        count = 0
5
6        for num in nums:
7            if count == 0:
8                candidate = num
9            if num == candidate:
10                count += 1
11            else:
12                count -= 1
13
14        return candidate