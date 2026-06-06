1class Solution:
2    def findShortestSubArray(self, nums: list[int]) -> int:
3        first = {}
4        last = {}
5        count = {}
6
7        for i, num in enumerate(nums):
8            if num not in first:
9                first[num] = i
10            last[num] = i
11            count[num] = count.get(num, 0) + 1
12
13        degree = max(count.values())
14        result = len(nums)
15
16        for num in count:
17            if count[num] == degree:
18                result = min(result, last[num] - first[num] + 1)
19
20        return result