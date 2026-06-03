1class Solution:
2    def findDuplicate(self, nums: list[int]) -> int:
3        low, high = 1, len(nums) - 1
4
5        while low < high:
6            mid = (low + high) // 2
7            count = 0
8
9            for num in nums:
10                if num <= mid:
11                    count += 1
12
13            if count > mid:
14                high = mid
15            else:
16                low = mid + 1
17
18        return low